from modules.functions import loadSettingsFile, getWindowPosition
from modules.feature_detection.bomb_detection import pickUpBomb, segmentBomb, solveModules
import time
import pyautogui


class Bomb:
    serial = ""
    batteries = ""
    ports = []

    # Modules will hold name and location on bomb
    modules = {}

    # Physical state will keep track of what is
    # being looked at on the bomb. That way, you
    # can go from any module to any other.
    # This should only be manipulated by
    # modules/controller/macro.py
    physical_state = None

    settings = {}

    def loadSettings(self):
        loadSettingsFile(self)

        if 'gameWindowLoc' not in self.settings:
            self.settings['gameWindowLoc'] = getWindowPosition()

        # while(1):
        #     time.sleep(0.2)
        #     print(self.settings)
        #     mousePos = pyautogui.position()
        #     x1 = int(self.settings['gameWindowLoc'][0])
        #     y1 = int(self.settings['gameWindowLoc'][1])
        #     x2 = int(self.settings['gameWindowLoc'][2])
        #     y2 = int(self.settings['gameWindowLoc'][3])

        #     # self.settings['gameWindowLoc'].spl
        #     print("{:.2f}, {:.2f}".format(
        #         (mousePos[0] - x1) / (x2 - x1), (mousePos[1] - y1) / (y2 - y1)))

    def initialAnalysis(self):
        pickUpBomb(self)
        segmentBomb(self)
        solveModules(self)
