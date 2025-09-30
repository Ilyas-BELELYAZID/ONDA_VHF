from PySide6.QtCore import QObject, QUrl
from PySide6.QtMultimedia import QSoundEffect
import os

class AlertSoundManager(QObject):
    def __init__(self, base_path="assets/sounds", parent=None):
        super().__init__(parent)
        self.base_path = base_path
        self.sounds = {
            "INFO": QSoundEffect(self),
            "WARNING": QSoundEffect(self),
            "CRITICAL": QSoundEffect(self),
        }
        mapping = {
            "INFO": "info.wav",
            "WARNING": "warning.wav",
            "CRITICAL": "critical.wav",
        }
        for level, filename in mapping.items():
            path = os.path.join(self.base_path, filename)
            if os.path.exists(path):
                url = QUrl.fromLocalFile(os.path.abspath(path))
                self.sounds[level].setSource(url)
                self.sounds[level].setLoopCount(1)
                self.sounds[level].setVolume(0.8)
            else:
                self.sounds[level].setSource(QUrl())
        self._muted = False

    def play(self, level="INFO"):
        if self._muted:
            return
        effect = self.sounds.get(level)
        if not effect or effect.source().isEmpty():
            try:
                from PySide6.QtWidgets import QApplication
                QApplication.beep()
            except Exception:
                pass
            return
        effect.play()

    def mute(self, yes=True):
        self._muted = bool(yes)

    def is_muted(self):
        return self._muted
