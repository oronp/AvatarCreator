import glob
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
NOTHING = [100, 120, 130]


def random_selector(list_of_objects):
    chosen = random.randint(0, len(list_of_objects) - 1)
    return cv.imread(list_of_objects[chosen])


def background_creator(shape, color):
    background = np.zeros((shape[0], shape[1], 3), np.uint8)
    changing_color(BLACK, color, background)
    return background


def changing_color(current_color, new_color, image):
    selected_color = np.all(image == current_color, axis=-1)  # the selected color.
    image[selected_color] = new_color


def add_avatar_part(current_avatar, added_object):
    test = np.any(added_object != BLACK, axis=-1)
    current_avatar[test] = added_object[test]
    return current_avatar


def draw_figure():
    background = background_creator([300, 300], NOTHING)
    direction_order = glob.glob('./images/*')
    direction_order.sort(key=lambda x: int(x.split('/')[-1].split('-')[0]))
    for single in direction_order:
        img = random_selector(glob.glob(single + '/*'))
        background = add_avatar_part(background, img)

    cv.imshow("image", background)
    cv.waitKey(0)


if __name__ == '__main__':
    draw_figure()
