from modules.feature_detection.functions import take_screenshot


def detectVisibleFeatures(bomb):
    # take screenshot
    screen = take_screenshot()

    # extract features (modules, ports, batteries)

    # add found features to bomb
