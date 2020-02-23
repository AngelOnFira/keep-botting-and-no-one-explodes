import cv2
import pyautogui
import numpy as np

from modules.feature_detection.functions import takeScreenshot, matchImages


def lstAvg(lst):
    return int(sum(lst) / len(lst))


def detectVisibleFeatures(bomb):
    # take screenshot
    screen = takeScreenshot()

    # extract features (modules, ports, batteries)

    # add found features to bomb


def findBomb():
    room = cv2.imread('images/room.png', 0)

    # TODO change this to full screen, this
    # is only for my second monitor
    screen = pyautogui.screenshot(region=(1920, 0, 1920, 1080))
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)

    matches = matchImages(room, screen, 10)

    x_list = []
    for point in matches:
        x_list.append(point[0][0])

    y_list = []
    for point in matches:
        y_list.append(point[0][1])

    return (lstAvg(x_list), lstAvg(y_list),)
