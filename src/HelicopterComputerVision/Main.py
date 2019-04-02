import os
import time
from src.HelicopterComputerVision import ScreenCollector


def start_firefox():
    os.system('firefox play-helicopter-game.com')


if __name__ == '__main__':
    time.sleep(5)
    start_time = time.time()
    for i in range(50):
        print(ScreenCollector.get_screen_data())
    print(time.time() - start_time)
