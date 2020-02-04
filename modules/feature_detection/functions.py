import pyautogui
import cv2


def take_screenshot():
    image = pyautogui.screenshot()
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
