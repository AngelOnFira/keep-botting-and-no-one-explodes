import cv2
import numpy as np
import time
from os import listdir
from os.path import isfile, join

from modules.feature_detection.functions import matchImages, averages, getPixelFromPercentage
from modules.feature_detection.memory import extract_text
from modules.controller.controller import clickAtLocation, moveToLocation, takeScreenshot, zoomOut
from modules.logic import button, memory, wires_complicated, wires_simple
from modules.controller.controller import SCREENSHOT_IMAGE_PATH
from modules.logic.memory import Memory, Stage, Instruction

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

if len(moduleReferences) != 11:
    raise Exception("Not 11")


def segmentBomb(bomb):
    # These were recorded manually. They represent the
    # top left and bottom right points as percentages
    # of the way across the screen
    moduleLocations = [
        [0.2759, 0.2562, 0.4382, 0.5128],
        [0.43, 0.26, 0.58, 0.50],
        [0.58, 0.26, 0.73, 0.50],
        [0.25, 0.51, 0.43, 0.77],
        [0.44, 0.51, 0.58, 0.76],
        [0.59, 0.51, 0.73, 0.76],
    ]

    x1 = getPixelFromPercentage(bomb, x=0.0)
    y1 = getPixelFromPercentage(bomb, y=0.0)
    x2 = getPixelFromPercentage(bomb, x=1.0)
    y2 = getPixelFromPercentage(bomb, y=1.0)

    # TODO this enumerate will only work for one side
    print("Detecting and capturing bomb modules...")
    for i, module in enumerate(moduleLocations):
        moduleFound = takeScreenshot(bomb, module, i)
        moduleGuess = detectModule(moduleFound)
        print(str(i + 1) + "th module: " + str(moduleGuess[2]))
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


def findMemoryModule(bomb):
    moduleCoords = [[0.35705,0.3845],[0.505,0.38],[0.655,0.38],[0.36,0.64],[0.51,0.635],[0.66,0.635]]
    module = None
    for k, m in bomb.modules.items():
        if m == "memory":
            module = k
    if module != None:
        clickAtLocation((
            getPixelFromPercentage(bomb, x=moduleCoords[module][0]),
            getPixelFromPercentage(bomb, y=moduleCoords[module][1]),
        ))

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
    for key, value in bomb.modules.items():
        if value == "simple-wires":
            pass
            # here I will call my simple wires functions
        elif value == "memory":
            findMemoryModule(bomb)
            solveMemoryModule(bomb, key)

def solveMemoryModule(bomb, moduleIdx):
    print("Solving memory module")

    solver = Memory()
    
    for level in range(1, 6):
        time.sleep(3) # wait for buttons to be setup
        screen = takeScreenshot(bomb)
        memory_module = screen[875:1500, 1645:2265]

        button_y = 663
        button_x = [872.5, 921, 969, 1020]
        
        # button_image_list = [button1, button2, button3, button4]
        display, buttons = extract_text(memory_module)
        buttons = buttons.replace('8', '3')
        buttons = buttons.replace('$', '3')

        # print("level: " + str(level))
        # print("display: " + str(display))
        # print("buttons: " + str(buttons))

        stage = Stage(level, int(display), [int(num) for num in buttons])
        solution = solver.stageSolution(stage)
        if solution.type == Instruction.Type.POSITION:
            # print("Solution Type = Position")
            buttonIndex = solution.value
        else:
            # print("Solution Type = Label")
            buttonIndex = buttons.index(str(solution.value)) + 1
        
        print("Button position to press: " + str(buttonIndex))

        clickAtLocation([button_x[buttonIndex - 1], button_y])
        moveToLocation([50,50])