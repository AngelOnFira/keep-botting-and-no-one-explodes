import time

from pyvirtualdisplay import Display
v_display = Display(visible=1, size=(1600,900))
v_display.start()
import pyautogui

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

def takeScreenshot(bomb, region=[0, 0, 1, 1]):
    image = pyautogui.screenshot(
        region=(
            getPixelFromPercentage(bomb, x=region[0]),
            getPixelFromPercentage(bomb, y=region[1]),
            getPixelFromPercentage(
                bomb, x=region[2]) - getPixelFromPercentage(bomb, x=region[0]),
            getPixelFromPercentage(
                bomb, y=region[3]) - getPixelFromPercentage(bomb, y=region[1])
        ),)
    cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(str(int(round(time.time() * 1000))) + "screen.png", cv_image)

    return cv_image