import threading
from src.HelicopterMovement import Navigator


class NavigatingThread(threading.Thread):
    def run(self):
        Navigator.update_helicopter_position()
