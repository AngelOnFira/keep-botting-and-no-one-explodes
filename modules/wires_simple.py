oddNumbers = ['1', '3', '5', '7', '9']


class WiresSimple:
    def __init__(self, moduleXY, serial):
        self.moduleXY = moduleXY
        self.serial = serial

    def solution(self, wires):
        if len(wires) == 3:
            if 'red' not in wires:
                self._cutWire(2)
            elif wires[-1] == 'white':
                self._cutWire(len(wires))
            elif wires.count('blue') > 1:
                self._cutLastColor('blue', wires)
            else:
                self._cutWire(len(wires))
        elif len(wires) == 4:
            if wires.count('red') > 1 and self.serial[-1] in oddNumbers:
                self._cutLastColor('red', wires)
            elif wires[-1] == 'yellow' and wires.count('red') == 0:
                self._cutWire(1)
            elif wires.count('blue') == 1:
                self._cutWire(1)
            elif wires.count('yellow') > 1:
                self._cutWire(len(wires))
            else:
                self._cutWire(2)
        elif len(wires) == 5:
            if wires[-1] == 'black' and self.serial[-1] in oddNumbers:
                self._cutWire(4)
            elif wires.count('red') == 1 and wires.count('yellow') > 1:
                self._cutWire(1)
            elif wires.count('black') == 0:
                self._cutWire(2)
            else:
                self._cutWire(1)
        elif len(wires) == 6:
            if wires.count('yellow') == 0 and self.serial[-1] in oddNumbers:
                self._cutWire(3)
            elif wires.count('yellow') and wires.count('white') > 1:
                pass

    def _cutWire(self, index):
        # TODO click at index
        # TODO fix position
        print("Simple Wires: I cut wire {} in position {}".format(index, 2))

    def _cutLastColor(self, color, wires):
        lastColor = wires[::-1].index(color)
        self._cutWire(lastColor)
