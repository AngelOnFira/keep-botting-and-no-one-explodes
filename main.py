import pyautogui
import time
import numpy as np
import imutils
import cv2

pyautogui.moveTo(1920/2, 600, duration=0.4)
pyautogui.leftClick()

screenshots = {}

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

def take_screenshot(name):
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    screenshots[name] = image

take_screenshot('test')

canny_output = cv2.Canny(screenshots['test'], 100, 200)

cv2.imshow("test", imutils.resize(canny_output, height=800))
cv2.waitKey(0)