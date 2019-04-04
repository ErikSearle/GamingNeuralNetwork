from src.HelicopterComputerVision.ScreenCollector import get_screen_data
from src.HelicopterMovement import Globals


def update_helicopter_position():
    """
    Asks the screen collector to provide the current information, and then updates the current and desired y positions
    of the helicopter accordingly. Currently it's set up to fly based on only updating the desired y position once for
    each block it encounters. The commented out sections show previous attempts.
    :return: Nothing
    """
    screen_data = get_screen_data()
    Globals.current_y_position = screen_data[2]
    if screen_data[3] is not None and (Globals.next_block_top is None or (Globals.next_block_top is not None and abs(Globals.next_block_top - screen_data[3][0]) > 5)):
        Globals.next_block_top = screen_data[3][0]
        next_block_front = screen_data[3][2]
        index_of_ceiling_above_block = (next_block_front - 240) // 15
        ceiling_above_block = screen_data[0][index_of_ceiling_above_block][1]
        floor_below_block = screen_data[1][index_of_ceiling_above_block][1]
        gap_above_block = screen_data[3][0] - ceiling_above_block
        gap_below_block = floor_below_block - screen_data[3][1]
        if (Globals.current_y_position < 400 and gap_above_block > 150) or gap_below_block < 150:
            Globals.desired_y_position = screen_data[3][0] + (gap_above_block // 2)
        else:
            Globals.desired_y_position = floor_below_block - (gap_below_block // 2)
    # if screen_data[3] is None:
    #     Globals.desired_y_position = 253
    # else:
    #     next_block_front = screen_data[3][2]
    #     index_of_ceiling_above_block = (next_block_front - 240) // 15
    #     ceiling_above_block = screen_data[0][index_of_ceiling_above_block][1]
    #     floor_below_block = screen_data[1][index_of_ceiling_above_block][1]
    #     gap_above_block = screen_data[3][0] - ceiling_above_block
    #     gap_below_block = floor_below_block - screen_data[3][1]
    #     if Globals.current_y_position < screen_data[3][0]:
    #         Globals.desired_y_position = min(Globals.current_y_position, screen_data[3][0] - 40)
    #     elif Globals.current_y_position > screen_data[3][1]:
    #         Globals.desired_y_position = min(Globals.current_y_position, floor_below_block - 40)
    #     elif gap_above_block > gap_below_block:
    #         Globals.desired_y_position = screen_data[3][0] - 60
    #     else:
    #         Globals.desired_y_position = floor_below_block - 60
    # if screen_data[3] is None or screen_data[3][0] > 150:
    #     Globals.desired_y_position = 150
    # else:
    #     Globals.desired_y_position = 200
