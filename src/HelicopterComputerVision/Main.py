import os
import time
from src.HelicopterComputerVision import ScreenCollector


def start_firefox():
    os.system('firefox play-helicopter-game.com')


if __name__ == '__main__':
    time.sleep(5)
    ScreenCollector.get_screen_data()
