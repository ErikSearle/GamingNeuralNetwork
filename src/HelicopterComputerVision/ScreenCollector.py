from fastgrab._linux_x11 import screenshot
import numpy
from matplotlib import pyplot as plt


def find_helicopter_game():
    img = numpy.zeros((509, 645, 4), 'uint8')
    screenshot(290, 184, img)
    fig, axes = plt.subplots(ncols=2, nrows=3,
                             figsize=(8, 4))
    ax0 = axes.flat
    ax0.imshow(img, cmap=plt.cm.gray)
