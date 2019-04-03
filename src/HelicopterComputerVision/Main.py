import os
import time
from src.HelicopterComputerVision import ScreenCollector
from src.HelicopterMovement import Navigator, Globals


def start_firefox():
    os.system('firefox play-helicopter-game.com')


if __name__ == '__main__':
    time.sleep(5)
    Navigator.update_helicopter_position()
    print(Globals.current_y_position, Globals.desired_y_position)
