import pyautogui
import time
import numpy as np
#import imutils
#import cv2

pyautogui.moveTo(1920/2, 600, duration=0.4)
pyautogui.leftClick()

pyautogui.leftClick()
pyautogui.drag(0, 400, button='right', duration=0.5)
pyautogui.sleep(1)
pyautogui.moveTo(1920/2, 1080/2, duration=0.1)
pyautogui.drag(0, -600, button='right', duration=0.5)
pyautogui.sleep(1)
pyautogui.moveTo(1920/2, 600, duration=0.1)
pyautogui.rightClick()
pyautogui.leftClick()

for i in range (2):
    pass


def rotate(dir):
    x = y = 0
    if dir == "left":
        x = -221
    if dir == "right":
        x = 221

# image = pyautogui.screenshot()
# image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)