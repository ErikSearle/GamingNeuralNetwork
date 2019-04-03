from pyautogui import moveTo, mouseUp, mouseDown
from time import sleep
from src.HelicopterMovement import Globals


# This is the main hover function for the helicopter
# It should move in a relatively straight line with this
from src.HelicopterMovement.Navigator import update_helicopter_position


def hover():
    '''
    # Now, the helicopter game is weird. If we send it a million clicks per second it will freak out
    # Therefore we do this thing where we pretend to hold the mouse button down for a bit and release
    # This is not perfect and is ass but that is the best we got
    # Feel free to tweak if necessary
    '''
    while in_correct_position():
        update_helicopter_position()
        mouseDown()
        sleep(0.03)
        mouseUp()
        sleep(0.003)


# This function is called in order to make the helicopter go down to avoid obstacles
def descend():
    while Globals.current_y_position < Globals.desired_y_position:
        update_helicopter_position()
        mouseUp()
        sleep(0.040)
        mouseDown()
        sleep(0.010)


# This function is called in order to make the helicopter move up to avoid obstacles
def ascend():
    while Globals.current_y_position > Globals.desired_y_position:
        update_helicopter_position()
        mouseDown()
        sleep(0.2)
        mouseUp()
        sleep(0.003)


def fly():
    moveTo(450, 430)
    while True:
        update_helicopter_position()
        if Globals.desired_y_position - 5 > Globals.current_y_position:
            # print("descend")
            descend()
        elif Globals.current_y_position - 5 > Globals.desired_y_position:
            # print("ascend")
            ascend()
        else:
            # print("hover", Globals.current_y_position, Globals.desired_y_position)
            hover()


def in_correct_position():
    if abs(Globals.desired_y_position - Globals.current_y_position) > 5:
        return False
    else:
        return True
