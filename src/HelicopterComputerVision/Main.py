import os
import time
from src.HelicopterComputerVision import ScreenCollector
from src.HelicopterMovement import Navigator, Globals


def start_firefox():
    """
    This method is not currently used, but would hypothetically allow the AI to open a web browser itself and start
    playing the game with no human interaction. To make this work, we would need to implement the ability to find the
    game wherever it appears in the screen
    :return:
    """
    os.system('firefox play-helicopter-game.com')


if __name__ == '__main__':
    """
        This method is here to allow us to test the computer vision aspects of the project
    """
    #This line allows time to switch to a web browser after the program starts and before the screen shot is taken
    time.sleep(5)
    Navigator.update_helicopter_position()
    print(Globals.current_y_position, Globals.desired_y_position)
