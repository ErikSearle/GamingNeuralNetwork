import threading
from src.HelicopterMovement import Navigator


class NavigatingThread(threading.Thread):
    def run(self):
        """
        This class and method hypothetically exist to allow the clicking of the mouse and the taking of screen shots to
        exist on separate threads, but in practice this created unpredictable results, so multithreading is not used in
        the current version
        :return: Nothing
        """
        Navigator.update_helicopter_position()
