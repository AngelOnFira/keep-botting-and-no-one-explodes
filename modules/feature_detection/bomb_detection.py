from modules.feature_detection.functions import takeScreenshot


def detectVisibleFeatures(bomb):
    # take screenshot
    screen = takeScreenshot()

    # extract features (modules, ports, batteries)

    # add found features to bomb
