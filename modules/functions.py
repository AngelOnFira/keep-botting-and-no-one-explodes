import os
import time
from modules.controller.controller import getMousePosition
import modules.feature_detection.bomb_detection


def loadSettingsFile(bomb):
    data = []
    if os.path.exists('settings.txt'):
        print("Loading game window location from settings.txt. Delete this file if you want to record the area again.")
        data = [line.strip()
                for line in open("settings.txt", 'r')]

    for item in data:
        itemSplit = item.split("=")
        bomb.settings[itemSplit[0]] = itemSplit[1].split(",")

    return data


def getWindowPosition():
    command = "none"
    firstPos = None
    secondPos = None
    while command != "":
        input('Press any key to record top left')
        firstPos = getMousePosition()

        input('Press any key to record bottom right')
        secondPos = getMousePosition()

        command = input(
            'Type "repeat" if you want to rerecord the locations: ')

    output = "gameWindowLoc={},{},{},{}".format(
        firstPos[0],
        firstPos[1],
        secondPos[0],
        secondPos[1],
    )

    file_object = open('settings.txt', 'a')
    file_object.write(output)
    file_object.close()

    return output.split("=")[1].split(",")


def pickUpBomb():
    bomb_detection.pickUpBomb()
