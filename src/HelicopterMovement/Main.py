from src.HelicopterMovement import pyrobot
from src.HelicopterComputerVision import ScreenCollector


def main():
    '''
     Thoughts for integrating the neural network, currently the decision is made in
     a while loop whether the helicopter hovers, ascends, or descends. That logic
     can be taken over by the neural net possibly and the neural net will tell the
     helicopter when to stop doing what it is doing and do something else :)
     '''
    # makes the robot so we can use its functions
    robot = pyrobot.Robot()

    #I used this to add a delay to the robot before my mouse was taken over
    robot.sleep(5)

    # This sets the mouse to roughly be in the middle of where the helicopter game is
    robot.set_mouse_pos(580, 350)

    #Main loop that runs the program
    while True:
        #first we get the screens data to decide what we want to do
        ceiling_positions, floor_positions, helicopter_position, block_position = ScreenCollector.get_screen_data()

        #if no obstacles dont do anything
        if helicopter_position != block_position:
            hover(robot)

        #if there is an obstacle and there is more space above the block than below it
        if helicopter_position == block_position and (ceiling_positions - block_position) > (block_position - floor_positions):
            ascend(robot)

        #if there is an obstacle and there is more space below the block than above it
        if helicopter_position == block_position and (ceiling_positions - block_position) < (block_position - floor_positions):
            descend(robot)

        #these functions are super simplistic but if these can work then they can be improved?
        #can add in whether or not it should move according to the slope of the floor/roof


# This is the main hover function for the helicopter
# It should move in a relatively straight line with this
def hover(robot):
    '''
    # Now, the helicopter game is weird. If we send it a million clicks per second it will freak out
    # Therefore we do this thing where we pretend to hold the mouse button down for a bit and release
    # This is not perfect and is ass but that is the best we got
    # Feel free to tweak if necessary
    '''

    # sets the obstacles boolean for the hover function. check_moves will return true or false depending on screen values
    no_obstacles = check_moves("hover")

    # performs shitty hovering until obstacles are detected
    while (no_obstacles):
        robot.mouse_down('left')
        robot.sleep(0.013)
        robot.mouse_up('left')
        robot.sleep(0.008)
        no_obstacles = check_moves("hover")


# This function is called in order to make the helicopter go down to avoid obstacles
def descend(robot):
    space_below = check_moves("descend")

    # While there is space between the helicopters y position and the space it wants to go to
    # we simply let the helicopter drop
    while (space_below):
        # do nothing until we reach where we want to go
        space_below = check_moves("descend")
    return

# This function is called in order to make the helicopter move up to avoid obstacles
def ascend(robot):
    space_above = check_moves("ascend")

    # "holds" down the mouse button until it is told not to
    while (space_above):
        robot.mouse_down('left')

    # release the mouse button before returning
    robot.mouse_up('left')
    return


#This is the main function that tells the flight functions what to do
def check_moves(descriptor):
    '''
    This function is called by each of the flight functions with a descriptor of what they are doing.
    The descriptor is used to decide what information is relevant to the helicopter currently.
    For example, the ascend function cares if it is getting close to the roof or if it has passed the block
    it is trying to avoid. We return a boolean that is used to control the loop of the current running function
    '''
    ceiling_positions, floor_positions, helicopter_position, block_position = ScreenCollector.get_screen_data()

    if descriptor == "ascend":
        if helicopter_position > block_position:
            return False
        else:
            return True

    if descriptor == "descend":
        if helicopter_position < block_position:
            return False
        else:
            return True

    if descriptor == "hover":
        if helicopter_position == block_position:
            return False
        else:
            return True

    #by default we return true to let the helicopter keep doing what it was doing
    return True

if __name__ == "__main__":
    main()
