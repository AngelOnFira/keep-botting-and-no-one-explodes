import cv2
import numpy as np
import time
from os import listdir
from os.path import isfile, join

from modules.feature_detection.functions import matchImages, averages, getPixelFromPercentage
from modules.controller.controller import clickAtLocation, moveToLocation, takeScreenshot
from modules.logic import button, memory, wires_complicated, wires_simple

MODULES_DIRECTORY = './images/modules'

# Load array of images from ./images/modules
moduleReferences = {}

for f in listdir(MODULES_DIRECTORY):
    fp = join(MODULES_DIRECTORY, f)
    if isfile(fp):
        fn = f.split(".")[0]
        if (fn == ""): # ignore the directory itself
            continue
        moduleReferences[fn] = cv2.imread(fp, 0)

if len(moduleReferences) != 10:
    raise Exception("Not 10")


def segmentBomb(bomb):
    # These were recorded manually. They represent the
    # top left and bottom right points as percentages
    # of the way across the screen
    moduleLocations = [
        [0.30, 0.26, 0.43, 0.50],
        [0.43, 0.26, 0.58, 0.50],
        [0.58, 0.26, 0.73, 0.50],
        [0.29, 0.51, 0.43, 0.77],
        [0.44, 0.51, 0.58, 0.76],
        [0.59, 0.51, 0.73, 0.76],
    ]

    moveToLocation((
        getPixelFromPercentage(bomb, x=0.0),
        getPixelFromPercentage(bomb, y=0.0),
    ))

    # TODO this enumerate will only work for one side
    for i, module in enumerate(moduleLocations):
        print(module)
        moduleFound = takeScreenshot(bomb, module)
        moduleGuess = detectModule(moduleFound)

        bomb.modules[i] = moduleGuess[2]

    # take a screnshot
    # segment into 6 images, this is deterministic
    # for each image, use detectModule() to see which one it is
    # add each model's info to the bomb object


def detectModule(moduleImg):
    # Have a module image passed in, figure out which one it is

    # Check moduleImg against each
    modulesMatches = []

    for key in moduleReferences.keys():
        # [[reference, sumDistance], ...]
        print("key:", key)
        print("ref:")
        print(moduleReferences[key])
        matches = matchImages(moduleImg, moduleReferences[key], 10)
        modulesMatches.append(
            (moduleReferences[key], sum([m.distance for m in matches[1]]), key))

    bestGuess = min(modulesMatches, key=lambda match: match[1])

    # Return most likely image
    return bestGuess


def detectVisibleFeatures(bomb):
    # take screenshot
    screen = takeScreenshot()

    # extract features (modules, ports, batteries)

    # add found features to bomb


def findMemoryModule():
    memory = cv2.imread('images/modules/memory.png', 0)

    clickAtLocation(averages(matchImages(memory, takeScreenshot(), 10)[0]))


def pickUpBomb(bomb):
    print(getPixelFromPercentage(bomb, x=0.5),
          getPixelFromPercentage(bomb, y=0.5))
    clickAtLocation((
        getPixelFromPercentage(bomb, x=0.5),
        getPixelFromPercentage(bomb, y=0.5),
    ))

    # Wait for the bomb to be picked up
    time.sleep(0.5)


def solveModules(bomb):
    for key, value in bomb.modules:
        if value == "simple-wires":
            pass
            # here I will call my simple wires functions
        elif value == "memory":
            pass
            # others can add their stuff in their own if
