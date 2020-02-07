from modules.bomb import Bomb
from modules.feature_detection.bomb_detection import detectVisibleFeatures

bomb = new Bomb()

# pick up the bomb

detectVisibleFeatures(bomb)

# rotate bomb to the other side

detectVisibleFeatures(bomb)

for module in bomb.modules:
    # solve the module
    # execute the solution
    pass
