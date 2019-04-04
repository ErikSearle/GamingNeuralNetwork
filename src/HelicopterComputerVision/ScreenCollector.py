from fastgrab._linux_x11 import screenshot
import numpy
from matplotlib import pyplot as plt


def get_screen_data():
    '''
    Takes a screen shot and parses out the data from the screen shot into a usable format.
    :return: ([roof positions], [floor positions], y_position_of_helicopter, y_position_of_next_block)
    '''
    img = numpy.zeros((509, 645, 4), 'uint8')
    screenshot(289, 227, img)
    ceiling_positions, floor_positions, helicopter_position, block_position = 0, 0, 0, 0
    try:
        ceiling_positions, floor_positions = get_ceiling_and_floor_positions(img)
        helicopter_position = get_helicopter_position(img, ceiling_positions[0][1], floor_positions[0][1])
        block_position = find_upcoming_block(img, ceiling_positions, floor_positions)
    except IndexError as e:
        print(e)
        show_image(img)
        exit(0)
    return ceiling_positions, floor_positions, helicopter_position, block_position


def get_ceiling_and_floor_positions(img):
    '''
    This method uses middle-out technology. It begins search in the middle of the screen and searches up and down to
    find the immediate edge of the ceiling and floor of the cave. It starts at the left side of the cave and moves right
    to get a list of ceiling and floor positions every 15 pixels.
    :param img: An image of helicopter game
    :return: ([ceiling_positions], [floor_positions])
    '''
    ceiling_positions = []
    floor_positions = []
    cave_height = 385
    y = 100
    for i in range(16, 43):
        x = i*15
        ceiling_edge_found = False
        while not ceiling_edge_found:
            if not numpy.array_equal(img[y][x], [102, 255, 102, 255]):
                y -= 5
            else:
                while not numpy.array_equal(img[y+1][x], [0, 0, 0, 255]):
                    y += 2
                ceiling_positions.append((x, y))
                ceiling_edge_found = True

        floor_edge_found = False
        while not floor_edge_found:
            if not numpy.array_equal(img[y+cave_height][x], [102, 255, 102, 255]):
                cave_height += 5
            else:
                while numpy.array_equal(img[y+cave_height-1][x], [102, 255, 102, 255]):
                    cave_height -= 5
                floor_positions.append((x, y+cave_height))
                floor_edge_found = True

    return ceiling_positions, floor_positions


def get_helicopter_position(img, ceiling_value, floor_value):
    '''
    Using the floor and ceiling values for the cave found at x value 240, this method searches the pixel column at
    x = 240 for the helicopter. It first finds the top of the helicopter, then the bottom, and takes the average of
    those values. When searching for the top of the helicopter we are looking for pixels that are not black or green. We
    have to include green here to ensure we don't accidentally read a block as the helicopter. When looking for the
    bottom, we see both black or green pixels as the bottom of the helicopter.
    :param img: The image to be searched
    :param ceiling_value: ceiling of the cave at x = 240
    :param floor_value: floor of the cave at x = 240
    :return: y value of the rough middle of the helicopter
    '''
    top_of_helicopter = -1
    bottom_of_helicopter = -1
    y = ceiling_value + 10
    while y < floor_value:
        if top_of_helicopter == -1:
            if not numpy.array_equal(img[y][240], [0, 0, 0, 255]) and not numpy.array_equal(img[y][240], [102, 255, 102, 255]):
                    top_of_helicopter = y
        elif numpy.array_equal(img[y][240], [0, 0, 0, 255]) or numpy.array_equal(img[y][240], [102, 255, 102, 255]):
            bottom_of_helicopter = y
            break
        y += 5
    return (bottom_of_helicopter + top_of_helicopter) // 2


def find_upcoming_block(img, ceiling_values, floor_values):
    """
    Using the floor and ceiling values already found, this method searches between the floor and ceiling to find the
    next upcoming block
    :param img: The image to be searched
    :param ceiling_values: list of ceiling values
    :param floor_values: list of floor values
    :return: position of next block or None if there is no block found
    """
    for column in range(len(ceiling_values)):
        block = find_block_in_column(img, ceiling_values[column][0], ceiling_values[column][1], floor_values[column][1])
        if block is not None:
            return block
    return None


def find_block_in_column(img, x, ceiling_value, floor_value):
    """
    Specifically searches a cloumn of pixels for a block
    :param img: Image to be searched
    :param x: x position of column
    :param ceiling_value: ceiling value in column
    :param floor_value: floor value in column
    :return: position of block, or None if block doesn't exist
    """
    y = ceiling_value+50
    while y < floor_value-50:
        if numpy.array_equal(img[y][x], [102, 255, 102, 255]):
            while numpy.array_equal(img[y][x], [102, 255, 102, 255]) or numpy.array_equal(img[y][x], [92, 230, 92, 255]):
                y -= 5
            top_of_block = y
            bottom_of_block = y + 100

            y += 20
            while numpy.array_equal(img[y][x], [102, 255, 102, 255]) or numpy.array_equal(img[y][x], [92, 230, 92, 255]):
                x -= 2
            front_of_block = x

            return top_of_block, bottom_of_block, front_of_block
        y += 50
    return None


def show_image(img):
    """
    This method exists for debugging purposes. It allows captured images to be displayed in image magic.
    :param img: The image to display
    :return: nothing
    """
    plt.imshow(img, interpolation='nearest')
    plt.imsave("helicopter.png", img)
    plt.show()
