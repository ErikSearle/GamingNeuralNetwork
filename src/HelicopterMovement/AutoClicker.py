from pyautogui import moveTo, mouseUp, mouseDown
from time import sleep
from src.HelicopterMovement import Globals
from src.HelicopterMovement.Navigator import update_helicopter_position


def hover():
    """
    Method used to make the helicopter hover at a single y position. Method uses pulse width modulation to hover.
    :return: Nothing
    """
    while in_correct_position():
        update_helicopter_position()
        mouseDown()
        sleep(0.03)
        mouseUp()
        sleep(0.003)


def descend():
    """
    Method used to make the helicopter descend. The method does not simply release the mouse and allow the helicopter to
    plummet, but instead uses an adjusted pulse width modulation to allow the helicopter to descend in a controlled way.
     This was neccesary to stop the helicopter from constantly crashing into the floor of the cave.
    :return: Nothing
    """
    while Globals.current_y_position < Globals.desired_y_position:
        update_helicopter_position()
        mouseUp()
        sleep(0.040)
        mouseDown()
        sleep(0.010)


def ascend():
    """
    Method used to make the helicopter ascend. The method again does not simply hold down the mouse button. For the same
    reason as descend, this help prevent the helicopter from flying into the ceiling.
    :return: Nothing
    """
    while Globals.current_y_position > Globals.desired_y_position:
        update_helicopter_position()
        mouseDown()
        sleep(0.2)
        mouseUp()
        sleep(0.003)


def fly():
    """
    Move's the mouse to the middle of the helicopter game and then controls which of the three flying methods get called
    in an infinite sequence to fly the helicopter.
    :return: Nothing
    """
    moveTo(450, 430)
    while True:
        update_helicopter_position()
        if Globals.desired_y_position - 5 > Globals.current_y_position:
            descend()
        elif Globals.current_y_position - 5 > Globals.desired_y_position:
            ascend()
        else:
            hover()


def in_correct_position():
    """
    A method used by the hover function to determine if the helicopters y position matches the helicopter's desired y
    position.
    :return: Nothing
    """
    if abs(Globals.desired_y_position - Globals.current_y_position) > 5:
        return False
    else:
        return True
