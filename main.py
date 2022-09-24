import glob
import random
import cv2 as cv
import numpy as np
import matplotlib as plt
import pandas as pd


COLORS = {
    'black': [0, 0, 0],
    'white': [255, 255, 255],
    'blue': [255, 0, 0],
    'green': [0, 255, 0],
    'brown': [100, 120, 130],
    'red': [0, 255, 0]
}


def random_selector(list_of_objects):
    chosen = random.randint(0, len(list_of_objects) - 1)
    #  choosing color -> need to be added
    return cv.imread(list_of_objects[chosen])


def background_creator(shape, color):
    background = np.zeros((shape[0], shape[1], 3), np.uint8)
    changing_color(COLORS['black'], color, background)
    return background


def changing_color(current_color, new_color, image):
    selected_color = np.all(image == current_color, axis=-1)  # the selected color.
    image[selected_color] = new_color


def add_avatar_part(current_avatar, added_object):
    mask = np.any(added_object != COLORS['black'], axis=-1)
    current_avatar[mask] = added_object[mask]
    return current_avatar


def draw_figure():
    avatar = background_creator([300, 300], COLORS['brown'])
    direction_order = glob.glob('./images/*')
    direction_order.sort(key=lambda x: int(x.split('/')[-1].split('-')[0]))
    for single in direction_order:
        img = random_selector(glob.glob(single + '/*'))
        avatar = add_avatar_part(avatar, img)

    cv.imshow("image", avatar)
    cv.waitKey(0)
    return avatar


if __name__ == '__main__':
    avatar = draw_figure()
