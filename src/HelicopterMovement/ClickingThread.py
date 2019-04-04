import threading
from src.HelicopterMovement import AutoClicker


class ClickingThread(threading.Thread):
    def run(self):
        """
        This class and method hypothetically exist to allow the clicking of the mouse and the taking of screen shots to
        exist on separate threads, but in practice this created unpredictable results, so multithreading is not used in
        the current version
        :return: Nothing
        """
        AutoClicker.fly()
