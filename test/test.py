from pymodbus.client import ModbusSerialClient

def test_slaves():
    print("\n🔌 Connexion aux esclaves ID=1,2,3 sur COM2")

    client = ModbusSerialClient(
        port="COM2",
        baudrate=9600,
        parity="N",
        stopbits=1,
        bytesize=8,
        timeout=1
    )

    if not client.connect():
        print("❌ Impossible de se connecter au port COM2")
        return

    try:
        # Boucle sur les esclaves 1, 2, 3
        for slave_id in [1, 2, 3]:
            print(f"\n📡 Test de l’esclave ID={slave_id}")

            # Lecture de 10 registres à partir de l’adresse 0
            result = client.read_holding_registers(address=0, count=6, device_id=slave_id)
            if not result.isError():
                print(f"✅ Valeurs lues de l’esclave {slave_id}: {result.registers}")
            else:
                print(f"❌ Erreur de lecture sur l’esclave {slave_id}")

            # Écriture d’une valeur dans le registre 2
            write = client.write_register(address=2, value=124 + slave_id, device_id=slave_id)
            if not write.isError():
                print(f"✍️ Valeur {124 + slave_id} écrite dans le registre 2 de l’esclave {slave_id}")
            else:
                print(f"❌ Erreur d’écriture sur l’esclave {slave_id}")

    finally:
        client.close()

test_slaves()
