import pyautogui
from modules.feature_detection.bomb_detection import detectVisibleFeatures, findBomb

# This should do all general movement on the bomb.


def moveTo(moduleNum, bomb):
    # This should move to a new module on
    # the bomb based on the current physical
    # state of the bomb
    pass


def pickUpBomb():
    location = findBomb()
    pyautogui.moveTo(location[0] + 1920, location[1],
                     0.3, pyautogui.easeInQuad)

    pyautogui.click()
