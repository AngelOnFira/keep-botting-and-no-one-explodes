from modules.bomb import Bomb
from modules.feature_detection.bomb_detection import detectVisibleFeatures, pickUpBomb, findMemoryModule, detectModule
from modules.feature_detection.functions import loadSettings, getWindowPosition

# bomb = new Bomb()

# global settings
# globals()['settings'] = loadSettings()

# print(globals())
# if 'gameWindowLoc' not in settings:
#     getWindowPosition()

# print(globals())

# exit()
import cv2
memory = cv2.imread('images/mazetest.png', 0)
image = detectModule(memory)
cv2.imshow("thign", image)
cv2.waitKey()
exit()

pickUpBomb()

findMemoryModule()

# detectVisibleFeatures(bomb)

# rotate bomb to the other side

# detectVisibleFeatures(bomb)

# for module in bomb.modules:
#     # solve the module
#     # execute the solution
#     pass
