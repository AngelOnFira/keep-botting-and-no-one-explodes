class Strip:

    def __init__(self, colour):
        self.colour = colour

class Button:

    def __init__(self, colour, text, button_state):
        self.colour = colour
        self.text = text
        self.button_state = button_state

    def pressButton(self, battery_count, label, indicator, strip, timer):

        if self.colour == 'blue' and self.text == 'Abort':
            return self.holdAndReleaseButton(strip, timer)

        elif battery_count > 1 and self.text == 'Detonate':
            return self.immediatelyHoldAndReleaseButton()

        elif self.colour == 'white' and label == 'CAR' and indicator == True:
            return self.holdAndReleaseButton(strip, timer)

        elif battery_count > 2 and indicator == True and label == 'FRK':
            return self.immediatelyHoldAndReleaseButton()

        elif self.colour == 'yellow':
            return self.holdAndReleaseButton(strip, timer)

        elif self.colour == 'red' and self.text == 'Hold':
            return self.immediatelyHoldAndReleaseButton()

        else:
            return self.holdAndReleaseButton(strip, timer)

    def holdAndReleaseButton(self, strip, timer):

        self.button_state = 'HELD'
        magic_number = self.checkStripColour(strip)
        self.checkTimer(timer, magic_number)
        return self.button_state

    def immediatelyHoldAndReleaseButton(self):

        self.button_state = 'HELD'
        self.button_state = 'RELEASED'
        return self.button_state

    def checkStripColour(self, strip):

        if strip.colour == "blue":
            return '4'
        elif strip.colour == "yellow":
            return '5'
        else:
            return '1'

    def checkTimer(self, timer, magic_number):

        if magic_number in timer:
            self.button_state = 'RELEASED'
        else:
            self.button_state = 'HELD'