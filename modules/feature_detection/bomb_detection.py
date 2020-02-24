import cv2
import pyautogui
import numpy as np
import time

from modules.feature_detection.functions import takeScreenshot, matchImages, averages
from modules.controller.controller import clickAtLocation


def detectVisibleFeatures(bomb):
    # take screenshot
    screen = takeScreenshot()

    # extract features (modules, ports, batteries)

    # add found features to bomb


def findMemoryModule():
    memory = cv2.imread('images/modules/memory.png', 0)

    clickAtLocation(averages(matchImages(memory, takeScreenshot(), 10)))


def pickUpBomb():
    room = cv2.imread('images/room.png', 0)

    coordinates = averages(matchImages(room, takeScreenshot(), 10))

    clickAtLocation(coordinates)

    # Wait for the bomb to be picked up
    time.sleep(0.5)
