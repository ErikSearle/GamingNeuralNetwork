from src.HelicopterComputerVision.ScreenCollector import get_screen_data
from src.HelicopterMovement import Globals


def update_helicopter_position():
    while True:
        screen_data = get_screen_data()
        Globals.current_y_position = screen_data[2]
        if screen_data[3] is None:
            Globals.desired_y_position = 296
        else:
            next_block_front = screen_data[3][2]
            index_of_ceiling_above_block = (next_block_front - 240) // 15
            ceiling_above_block = screen_data[0][index_of_ceiling_above_block][1]
            floor_below_block = screen_data[1][index_of_ceiling_above_block][1]
            gap_above_block = screen_data[3][0] - ceiling_above_block
            gap_below_block = floor_below_block - screen_data[3][1]
            if gap_above_block > gap_below_block:
                Globals.desired_y_position = ceiling_above_block + gap_above_block // 2
            else:
                Globals.desired_y_position = screen_data[3][1] + gap_below_block // 2
