import os
import time
from src.HelicopterComputerVision import ScreenCollector


def start_firefox():
    os.system('firefox play-helicopter-game.com')


if __name__ == '__main__':
    time.sleep(2)
    ScreenCollector.find_helicopter_game()
