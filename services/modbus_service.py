import asyncio
import inspect
import logging
from pymodbus.client import AsyncModbusSerialClient

logger = logging.getLogger(__name__)

class ModbusService:
    def __init__(self,
                 port: str = "COM2",
                 baudrate: int = 9600,
                 parity: str = "N",
                 stopbits: int = 1,
                 bytesize: int = 8,
                 timeout: float = 1.0,
                 device_id: int = 1):
        self.port = port
        self.baudrate = baudrate
        self.parity = parity
        self.stopbits = stopbits
        self.bytesize = bytesize
        self.timeout = timeout
        self.device_id = device_id
        self.client: AsyncModbusSerialClient | None = None

    async def connect(self) -> bool:
        """Établit une connexion Modbus RTU asynchrone."""
        try:
            self.client = AsyncModbusSerialClient(
                port=self.port,
                baudrate=self.baudrate,
                parity=self.parity,
                stopbits=self.stopbits,
                bytesize=self.bytesize,
                timeout=self.timeout
            )
            connected = await self.client.connect()
            if not connected:
                logger.error("❌ Impossible de se connecter au port %s", self.port)
            else:
                logger.info("✅ Connecté au port %s (baudrate=%d)", self.port, self.baudrate)
            return connected
        except Exception as e:
            logger.exception("Erreur de connexion Modbus RTU: %s", e)
            return False

    async def read_holding(self, address: int, count: int = 1):
        """Lire des registres holding"""
        if not self.client:
            return None
        try:
            result = await self.client.read_holding_registers(address=address, count=count, device_id=self.device_id)
            if result.isError():
                logger.warning("Erreur lecture holding: %s", result)
                return None
            return result.registers
        except Exception as e:
            logger.exception("Exception read_holding: %s", e)
            return None

    async def write_register(self, address: int, value: int) -> bool:
        """Écrire un registre unique"""
        if not self.client:
            return False
        try:
            write = await self.client.write_register(address=address, value=value, device_id=self.device_id)
            if write.isError():
                logger.warning("Erreur écriture registre %d: %s", address, write)
                return False
            return True
        except Exception as e:
            logger.exception("Exception write_register: %s", e)
            return False

    async def write_registers(self, address: int, values: list[int]) -> bool:
        """Écrire plusieurs registres"""
        if not self.client:
            return False
        try:
            writes = await self.client.write_registers(address=address, values=values, device_id=self.device_id)
            if writes.isError():
                logger.warning("Erreur écriture registres à %d: %s", address, writes)
                return False
            return True
        except Exception as e:
            logger.exception("Exception write_registers: %s", e)
            return False

    async def scan_devices(self, start: int = 1, end: int = 247, address: int = 0, count: int = 1, delay: float = 0.05, connect_if_needed: bool = True, progress_callback=None) -> list[int]:
        """
            Scanner la plage d'ID Modbus [start..end] en interrogeant read_holding_registers(address, count).
            - address/count : registres à lire (certains appareils peuvent ne pas répondre à cette fonction)
            - delay : délai (s) entre requêtes pour laisser le bus respirer (0.05 ~ 50 ms)
            - connect_if_needed : si True -> essayer connect() si pas encore connecté
            - progress_callback : fonction(optionnelle) appelée comme progress_callback(device_id, ok)
            Retour : liste d'IDs ayant répondu correctement.
        """
        # s'assurer connecté si demandé
        if connect_if_needed and (self.client is None):
            ok = await self.connect()
            if not ok:
                return []

        found = []
        # Itérer chaque ID séquentiellement — le bus série n'aime pas les requêtes concurrentes
        for dev_id in range(start, end + 1):
            try:
                resp = await self.client.read_holding_registers(address=address, count=count, device_id=dev_id)
                # resp peut être None ou contenir isError()
                if resp is not None and not getattr(resp, "isError", lambda: False)():
                    found.append(dev_id)
                    if progress_callback:
                        try:
                            progress_callback(dev_id, True)
                        except Exception:
                            pass
                else:
                    if progress_callback:
                        try:
                            progress_callback(dev_id, False)
                        except Exception:
                            pass
            except Exception:
                # toute exception considérée comme pas de réponse
                if progress_callback:
                    try:
                        progress_callback(dev_id, False)
                    except Exception:
                        pass
            # petite pause pour éviter de saturer le bus / donner le temps à l'esclave
            await asyncio.sleep(delay)
        return found

    async def count_devices(self, *args, **kwargs) -> tuple[int, list[int]]:
        """
        Wrapper qui retourne (count, list_of_ids).
        Arguments passés à scan_devices.
        """
        found = await self.scan_devices(*args, **kwargs)
        return len(found), found

    async def close(self):
        """Ferme la connexion Modbus de façon robuste (supporte close sync ou async)."""
        if not self.client:
            logger.debug("close(): pas de client Modbus à fermer.")
            return

        try:
            close_method = getattr(self.client, "close", None)
            if close_method is None or not callable(close_method):
                logger.warning("Le client Modbus n'a pas de méthode close() callable.")
            else:
                try:
                    result = close_method()
                except TypeError:
                    # Certains clients exigent des args ou ferment différemment — log et continuer
                    logger.exception("Erreur en appelant client.close() (TypeError).")
                    result = None

                # Si la méthode renvoie une coroutine/future -> await it
                if inspect.isawaitable(result):
                    try:
                        await result
                    except Exception:
                        logger.exception("Exception lors de l'await de client.close().")
                else:
                    # méthode sync (ou None) : on laisse le temps aux tâches internes de se terminer
                    # un petit sleep(0) permet de céder le contrôle à l'event loop
                    await asyncio.sleep(0)

            # Certains backends ont un 'transport' ou 'protocol' à fermer explicitement
            # (optionnel, selon implémentation)
            try:
                transport = getattr(self.client, "transport", None)
                if transport and hasattr(transport, "close"):
                    transport.close()
            except Exception:
                pass

            logger.info("ModbusService: client fermé.")
        except Exception as e:
            logger.exception("Erreur fermeture client Modbus: %s", e)
        finally:
            # s'assurer de nettoyer la référence
            self.client = None