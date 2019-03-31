import threading
from src.HelicopterMovement import AutoClicker


class ClickingThread(threading.Thread):
    def run(self):
        AutoClicker.fly()
