import pyautogui
import time

# This should do all general movement on the bomb.


def moveTo(moduleNum, bomb):
    # This should move to a new module on
    # the bomb based on the current physical
    # state of the bomb
    pass


def clickAtLocation(location):
    pyautogui.moveTo(location[0], location[1], 0.3, pyautogui.easeInQuad)
    pyautogui.click()


def moveToLocation(location):
    pyautogui.moveTo(location[0], location[1], 0.1, pyautogui.easeInQuad)


def getMousePosition():
    return pyautogui.position()
