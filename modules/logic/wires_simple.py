oddNumbers = ['1', '3', '5', '7', '9']


class WiresSimple:
    wires = []
    positions = []
    bomb = None

    def solution(self, wiresOnModule, bomb):

        instanceWires = []
        instancePositions = []
        solution = None

        for i, wire in enumerate(wiresOnModule):
            if wire == '':
                continue

            instanceWires.append(wire)
            instancePositions.append(i + 1)

        self.wires = instanceWires
        self.positions = instancePositions
        self.bomb = bomb

        if len(self.wires) == 3:
            if 'red' not in self.wires:
                self._cutWire(2)
            elif self.wires[-1] == 'white':
                self._cutWire(len(self.wires))
            elif self.wires.count('blue') > 1:
                self._cutLastColor('blue')
            else:
                self._cutWire(len(self.wires))
        elif len(self.wires) == 4:
            if self.wires.count('red') > 1 and self.bomb.serial[-1] in oddNumbers:
                self._cutLastColor('red')
            elif self.wires[-1] == 'yellow' and self.wires.count('red') == 0:
                self._cutWire(1)
            elif self.wires.count('blue') == 1:
                self._cutWire(1)
            elif self.wires.count('yellow') > 1:
                self._cutWire(len(self.wires))
            else:
                self._cutWire(2)
        elif len(self.wires) == 5:
            if self.wires[-1] == 'black' and self.bomb.serial[-1] in oddNumbers:
                self._cutWire(4)
            elif self.wires.count('red') == 1 and self.wires.count('yellow') > 1:
                self._cutWire(1)
            elif self.wires.count('black') == 0:
                self._cutWire(2)
            else:
                self._cutWire(1)
        elif len(self.wires) == 6:
            if self.wires.count('yellow') == 0 and self.bomb.serial[-1] in oddNumbers:
                self._cutWire(3)
            elif self.wires.count('yellow') and self.wires.count('white') > 1:
                pass

        return self.solution

    def _cutWire(self, index):
        print("Simple Wires: I cut wire {} in position {}".format(
            index, self.positions[index - 1]))

        self.solution = (self.positions[index - 1])

    def _cutLastColor(self, color):
        lastColor = len(self.wires) - self.wires[::-1].index(color)
        self._cutWire(lastColor)
