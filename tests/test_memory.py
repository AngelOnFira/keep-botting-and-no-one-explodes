import pytest
from modules.logic.memory import Memory, Stage, Instruction

module = 'Memory'

def test_1(capsys):

    stages = [
        Stage(1, 1, [2, 4, 2, 1]),
        Stage(2, 2, [3, 1, 4, 2]),
        Stage(3, 3, [4, 1, 2, 3]),
        Stage(4, 1, [3, 4, 1, 2]),
        Stage(5, 3, [3, 2, 4, 1])
    ]

    solutions = [
        Instruction(Instruction.Type.POSITION, 2),
        Instruction(Instruction.Type.POSITION, 2),
        Instruction(Instruction.Type.POSITION, 3),
        Instruction(Instruction.Type.POSITION, 2),
        Instruction(Instruction.Type.LABEL, 4)
    ]

    run_test(stages, solutions)

def test_2(capsys):

    stages = [
        Stage(1, 2, [1, 4, 2, 3]),
        Stage(2, 1, [2, 3, 1, 4]),
        Stage(3, 4, [3, 2, 1, 4]),
        Stage(4, 1, [1, 3, 4, 2]),
        Stage(5, 4, [4, 3, 2, 1])
    ]

    solutions = [
        Instruction(Instruction.Type.POSITION, 2),
        Instruction(Instruction.Type.LABEL, 4),
        Instruction(Instruction.Type.LABEL, 4),
        Instruction(Instruction.Type.POSITION, 2),
        Instruction(Instruction.Type.LABEL, 4)
    ]

    run_test(stages, solutions)

def test_3(capsys):

    stages = [
        Stage(1, 4, [4, 3, 1, 2]),
        Stage(2, 2, [4, 1, 2, 3]),
        Stage(3, 3, [4, 3, 1, 2]),
        Stage(4, 4, [2, 4, 1, 3]),
        Stage(5, 3, [2, 3, 4, 1])
    ]

    solutions = [
        Instruction(Instruction.Type.POSITION, 4),
        Instruction(Instruction.Type.POSITION, 4),
        Instruction(Instruction.Type.POSITION, 3),
        Instruction(Instruction.Type.POSITION, 4),
        Instruction(Instruction.Type.LABEL, 3)
    ]

    run_test(stages, solutions)

def test_4(capsys):

    stages = [
        Stage(1, 2, [3, 1, 2, 4]),
        Stage(2, 4, [3, 2, 4, 1]),
        Stage(3, 4, [2, 4, 1, 3]),
        Stage(4, 4, [1, 4, 3, 2]),
        Stage(5, 4, [4, 1, 2, 3])
    ]

    solutions = [
        Instruction(Instruction.Type.POSITION, 2),
        Instruction(Instruction.Type.POSITION, 2),
        Instruction(Instruction.Type.LABEL, 4),
        Instruction(Instruction.Type.POSITION, 2),
        Instruction(Instruction.Type.LABEL, 4)
    ]

    run_test(stages, solutions)

def run_test(stages, solutions):
    solver = Memory()

    for i in range(5):
        try:
            stage = stages[i]
            given_instruction = solver.stageSolution(stage)
            expected_instruction = solutions[i]
            assert given_instruction == expected_instruction
        except AssertionError as e:
            e.args += ("Memory", "Failed at Stage " + str(stage.num) + " (" + str(stage.display) + ", " + str(stage.labels) + ")",
                "Given: (" + str(given_instruction.type) + ", " + str(given_instruction.value) + ")",
                "Expecting: (" + str(expected_instruction.type) + ", " + str(expected_instruction.value) + ")",
                "Label history: " + str(solver.stageLabelHistory),
                "Position history: " + str(solver.stagePositionHistory))
            raise
