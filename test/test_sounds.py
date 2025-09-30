import sys
import os
from PySide6.QtCore import QUrl, QTimer
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class SoundTester(QWidget):
    """
    Un widget de test qui joue une liste de sons en séquence, de manière non-bloquante.
    """
    def __init__(self, sound_files):
        super().__init__()
        if not sound_files:
            raise ValueError("La liste des fichiers son ne peut pas être vide.")
        self.sound_files = sound_files
        self.current_sound_index = -1
        self.sound_effects = [] # Liste pour garder les objets en mémoire

        self._setup_ui()

        # Lancer la lecture du premier son après un court délai pour que la fenêtre s'affiche
        QTimer.singleShot(500, self.play_next_sound)

    def _setup_ui(self):
        """Configure l'interface simple pour afficher l'état."""
        self.setWindowTitle("Testeur d'Alertes Sonores")
        self.layout = QVBoxLayout(self)
        self.status_label = QLabel("Initialisation...")
        self.layout.addWidget(self.status_label)
        self.resize(300, 100)

    def play_next_sound(self):
        """
        Joue le son suivant dans la liste. S'arrête quand la liste est terminée.
        """
        self.current_sound_index += 1
        if self.current_sound_index >= len(self.sound_files):
            self.status_label.setText("Test terminé. Fermeture...")
            print("[INFO] Tous les sons ont été joués.")
            # Fermer l'application après une seconde
            QTimer.singleShot(1000, self.close)
            return

        sound_file = self.sound_files[self.current_sound_index]

        if not os.path.exists(sound_file):
            print(f"[ERREUR] Le fichier '{sound_file}' est introuvable. Passage au suivant.")
            self.status_label.setText(f"Erreur: {os.path.basename(sound_file)} introuvable.")
            # Attendre un peu avant de passer au son suivant
            QTimer.singleShot(1500, self.play_next_sound)
            return

        # Créer un nouvel objet QSoundEffect et le garder en mémoire
        sound = QSoundEffect()
        sound.setSource(QUrl.fromLocalFile(sound_file))
        sound.setVolume(0.9) # Volume à 90%

        # Le garder en mémoire pour éviter qu'il ne soit détruit par le garbage collector
        self.sound_effects.append(sound)

        # Connexion du signal 'playingChanged' pour détecter la fin de la lecture
        # Quand le son s'arrête, 'playingChanged' est émis. Si le son n'est plus en lecture,
        # on appelle play_next_sound.
        sound.playingChanged.connect(lambda: self.on_playing_changed(sound))

        sound.play()

        # Vérifier si le son a bien été chargé
        if sound.status() != QSoundEffect.Ready:
            print(f"[AVERTISSEMENT] Le son '{sound_file}' n'est pas prêt, il pourrait ne pas se jouer.")

        print(f"[OK] Lecture de '{sound_file}'...")
        self.status_label.setText(f"En cours de lecture :\n{os.path.basename(sound_file)}")
    def on_playing_changed(self, sound_effect):
        """Slot appelé quand l'état de lecture d'un son change."""
        if not sound_effect.isPlaying():
            # Déconnecter le signal pour éviter les appels multiples
            sound_effect.playingChanged.disconnect()
            # Lancer le son suivant
            self.play_next_sound()


if __name__ == "__main__":
    # Assurez-vous d'avoir un dossier "assets/sounds" à côté de ce script,
    # contenant les fichiers "info.wav", "warning.wav", et "critical.wav".

    app = QApplication(sys.argv)

    sound_folder = "assets/sounds"
    sound_filenames = ["info.wav", "warning.wav", "critical.wav", "non_existent_file.wav"]
    sound_paths = [os.path.join(sound_folder, f) for f in sound_filenames]

    tester = SoundTester(sound_paths)
    tester.show()

    sys.exit(app.exec())