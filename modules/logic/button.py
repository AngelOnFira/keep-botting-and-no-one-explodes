from enum import Enum

## This indicator class should be moved out to a separate script in the future
##  since it should first be stored by the Defuser when the game begins

class Indicator:

    def __init__(self, is_on, label):
        self.is_on = is_on
        self.label = label

class Button:

    # Button colours:
    #   Blue, Red, White, Yellow, Black

    # Strip colours:
    #   Blue, Red, White, Yellow

    # Button lables:
    #   Abort, Detonate, Hold, Press

    Colour = Enum('Colour', 'BLUE, RED, WHITE, YELLOW, BLACK')

    def __init__(self, num_batteries, indicator, button_colour, button_label):
        self.num_batteries = num_batteries
        self.indicator = indicator
        self.button_colour = button_colour
        self.button_label = button_label

    def getPressAction(self):

        holdCallback = None

        # Must be checked IN ORDER as they appear in the manual
        if (self.button_colour is Button.Colour.BLUE and self.button_label is "Abort"):
            holdCallback = self.pressAndHoldCallback
        elif (self.num_batteries > 1 and self.button_label is "Detonate"):
            holdCallback = None
        elif (self.button_colour is Button.Colour.WHITE and self.isIndicator(True, "CAR")):
            holdCallback = self.pressAndHoldCallback
        elif (self.num_batteries > 2 and self.isIndicator(True, "FRK")):
            holdCallback = None
        elif (self.button_colour is Button.Colour.YELLOW):
            holdCallback = self.pressAndHoldCallback
        elif (self.button_colour is Button.Colour.RED and self.button_label is "Hold"):
            holdCallback = None
        else:
            holdCallback = self.pressAndHoldCallback

        return holdCallback

    def pressAndHoldCallback(self, indicator_colour):
        timerNum = -1

        if (indicator_colour is Button.Colour.BLUE):
            timerNum = 4
        elif (indicator_colour is Button.Colour.YELLOW):
            timerNum = 5
        else:
            timerNum = 1

        return timerNum

    def isIndicator(self, is_on, label):
        if (self.indicator is None):
            return False

        return (self.indicator.is_on == is_on and self.indicator.label == label)
