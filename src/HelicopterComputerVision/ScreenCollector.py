from fastgrab._linux_x11 import screenshot
import numpy
from matplotlib import pyplot as plt
from time import time


def find_helicopter_game():
    img = numpy.zeros((509, 645, 4), 'uint8')
    screenshot(290, 184, img)
    colors = []
    for i in range(509):
        unique_rows = numpy.vstack(tuple({tuple(row) for row in img[i]}))
        for color in unique_rows:
            colors.append(color)
    unique_colours = {tuple(row) for row in colors}
    print(len(unique_colours))
    print(colors)
    # list_of_colours = []
    # for i in range(509):
    #     if i%50 == 0:
    #         print(i)
    #     for j in range(64):
    #         oneD = OneDArray(img[i][j*10])
    #         if oneD not in list_of_colours:
    #             list_of_colours.append(oneD)
    # print(len(list_of_colours))
    # for colour in list_of_colours:
    #     print(colour)
    # for i in range(509):
    #     for j in range(645):
    #         img[i][j] = [102, 255, 102, 255]
    plt.imshow(img, interpolation='nearest')
    plt.imsave("helicopter.png", img)
    plt.show()


def get_screen_data():
    '''
    Takes a screen shot and parses out the data from the screen shot into a usable format.
    :return: ([roof positions], [floor positions], y_position_of_helicopter, y_position_of_next_block)
    '''
    start_time = time()
    img = numpy.zeros((509, 645, 4), 'uint8')
    screenshot(290, 184, img)
    show_image(img)
    ceiling_positions, floor_positions = get_ceiling_and_floor_positions(img)
    print(time() - start_time)

    for i in range(len(ceiling_positions)):
        print((ceiling_positions[i], floor_positions[i]))
    # floor_positions = get_floor_positions(img)
    # helicopter_position = get_helicopter_position(img)
    # next_block_position = get_next_block_position(img)
    # return (roof_positions, floor_positions, helicopter_position, next_block_position)
    # print(roof_positions)


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
    cave_height = 200
    y = 100
    for i in range(16, 34):
        x = i*15
        ceiling_edge_found = False
        while not ceiling_edge_found:
            if numpy.array_equal(img[y][x], [0, 0, 0, 255]):
                y -= 5
            elif not numpy.array_equal(img[y][x], [102, 255, 102, 255]):
                y -= 1
            else:
                while numpy.array_equal(img[y+1][x], [102, 255, 102, 255]):
                    y += 1
                ceiling_positions.append((x, y))
                ceiling_edge_found = True

        floor_edge_found = False
        while not floor_edge_found:
            if numpy.array_equal(img[y+cave_height][x], [0, 0, 0, 255]):
                cave_height += 5
            elif not numpy.array_equal(img[y+cave_height][x], [102, 255, 102, 255]):
                cave_height += 1
            else:
                while numpy.array_equal(img[y+cave_height-1][x], [102, 255, 102, 255]):
                    cave_height -= 1
                floor_positions.append((x, y+cave_height))
                floor_edge_found = True

    return ceiling_positions, floor_positions
    # roof_positions = []
    # current_y_value = 50
    # for x in range(2, 51):
    #     current_x_value = x*10
    #     green_black_edge_found = False
    #     while not green_black_edge_found:
    #         if numpy.array_equal(img[current_y_value][current_x_value], [102, 255, 102, 255]):
    #             if numpy.array_equal(img[current_y_value+5][current_x_value], [0, 0, 0, 255]):
    #                 roof_positions.append((current_y_value, current_x_value))
    #                 green_black_edge_found = True
    #             else:
    #                 current_y_value += 5
    #         elif numpy.array_equal(img[current_y_value+5][current_x_value], [0, 0, 0, 255]):
    #             current_y_value -= 5
    #         else:
    #             current_y_value += 5
    # return roof_positions




def show_image(img):
    plt.imshow(img, interpolation='nearest')
    plt.imsave("helicopter.png", img)
    plt.show()
