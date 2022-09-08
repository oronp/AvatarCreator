import random
import cv2 as cv
import numpy as np
import matplotlib as plt
import pandas as pd
import Objects


BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
BLUE = [255, 0, 0]
GREEN = [0, 255, 0]


def changing_color(current_color, new_color, image):
    selected_color = np.all(image == current_color, axis=-1)  # the selected color.
    image[selected_color] = new_color
    return image


if __name__ == '__main__':
    first = Objects.Background()
    black_square = np.zeros((1080, 1080, 3), np.uint8)
    for i in range(8):
        a = i * 135
        cv.rectangle(black_square, (0 + a, 0 + a), (135 + a, 135 + a), WHITE, -1)
    cv.circle(black_square, (650, 350), 75, GREEN, -1)
    black_square = changing_color(GREEN, BLUE, black_square)
    cv.imshow("shaked", black_square)
    cv.waitKey(0)
    pass