#oddNumbers = ['1', '3', '5', '7', '9']
from enum import Enum

# Defines the current stage (1-5)
class Stage:

    def __init__(self, num, display, labels):
        self.num = num
        self.display = display
        self.labels = labels

# Defines the instruction to be returned to the player
class Instruction:

    Type = Enum('Type', 'LABEL, POSITION')

    def __init__(self, type, value):
        self.type = type
        self.value = value

    # implement custom equality check for testing
    def __eq__(self, other):
        if isinstance(other, Instruction):
            print("isinstance")
            return self.type == other.type and self.value == other.value
        print("NOT AN INSTANCE")
        return False

# Defines the module solver
class Memory:

    # Keep track of previous stage instructions
    stageLabelHistory = { 1: None, 2: None, 3: None, 4: None }
    stagePositionHistory = { 1: None, 2: None, 3: None, 4: None }

    def __init__(self):
        pass

    # provide the solution for the provided stage
    def stageSolution(self, stage):
        if (stage.num == 1):
            if    (stage.display == 3):
                solution = Instruction(Instruction.Type.POSITION, 3)
            elif  (stage.display == 4):
                solution = Instruction(Instruction.Type.POSITION, 4)
            else: #display is 1 or 2
                solution = Instruction(Instruction.Type.POSITION, 2)
        elif (stage.num == 2):
            if   (stage.display == 1):
                solution = Instruction(Instruction.Type.LABEL, 4)
            elif (stage.display == 3):
                solution = Instruction(Instruction.Type.POSITION, 1)
            else: #display is 2 or 4
                solution = Instruction(Instruction.Type.POSITION, self.stagePositionHistory[1])
        elif (stage.num == 3):
            if   (stage.display == 1):
                solution = Instruction(Instruction.Type.LABEL, self.stageLabelHistory[2])
            elif (stage.display == 2):
                solution = Instruction(Instruction.Type.LABEL, self.stageLabelHistory[1])
            elif (stage.display == 3):
                solution = Instruction(Instruction.Type.POSITION, 3)
            else: #display is 4
                solution = Instruction(Instruction.Type.LABEL, 4)
        elif (stage.num == 4):
            if   (stage.display == 1):
                solution = Instruction(Instruction.Type.POSITION, self.stagePositionHistory[1])
            elif (stage.display == 2):
                solution = Instruction(Instruction.Type.POSITION, 1)
            else: #display is 3 or 4
                solution = Instruction(Instruction.Type.POSITION, self.stagePositionHistory[2])
        else: #stage is 5
            if   (stage.display == 3):
                solution = Instruction(Instruction.Type.LABEL, self.stageLabelHistory[4])
            elif (stage.display == 4):
                solution = Instruction(Instruction.Type.LABEL, self.stageLabelHistory[3])
            else: #display is 1 or 2
                solution = Instruction(Instruction.Type.LABEL, self.stageLabelHistory[stage.display])

        # store info that might become relevent in future stages
        if (stage.num < 5):
            if (solution.type == Instruction.Type.POSITION):
                self.stagePositionHistory[stage.num] = solution.value
                self.stageLabelHistory[stage.num] = stage.labels[solution.value-1]
            else: # solution type is LABEL
                self.stagePositionHistory[stage.num] = stage.labels.index(solution.value-1)
                self.stageLabelHistory[stage.num] = solution.value

        return solution
