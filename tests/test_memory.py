import pytest
from modules.logic.memory import Memory, Stage, Instruction

module = 'Memory'

# Field tests are taken from real KTANE gameplay
# Synthetic tests are there to shore up missing code coverage

def test_field_1(capsys):

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

    run_test("test_field_1", stages, solutions)

def test_field_2(capsys):

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

    run_test("test_field_2", stages, solutions)

def test_field_3(capsys):

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

    run_test("test_field_3", stages, solutions)

def test_field_4(capsys):

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

    run_test("test_field_4", stages, solutions)

def test_synthetic_1(capsys):

    stages = [
        Stage(1, 3, [3, 1, 2, 4]),
        Stage(2, 1, [1, 2, 4, 3]),
        Stage(3, 1, [2, 3, 4, 1]),
        Stage(4, 1, [4, 3, 1, 2]),
        Stage(5, 1, [3, 2, 4, 1])
    ]

    solutions = [
        Instruction(Instruction.Type.POSITION, 3),
        Instruction(Instruction.Type.LABEL, 4),
        Instruction(Instruction.Type.LABEL, 4),
        Instruction(Instruction.Type.POSITION, 3),
        Instruction(Instruction.Type.LABEL, 2)
    ]

    run_test("test_synthetic_1", stages, solutions)

def test_synthetic_2(capsys):

    stages = [
        Stage(1, 3, [3, 1, 2, 4]),
        Stage(2, 1, [1, 2, 4, 3]),
        Stage(3, 2, [2, 3, 4, 1]),
        Stage(4, 4, [4, 3, 1, 2]),
        Stage(5, 2, [3, 2, 4, 1])
    ]

    solutions = [
        Instruction(Instruction.Type.POSITION, 3),
        Instruction(Instruction.Type.LABEL, 4),
        Instruction(Instruction.Type.LABEL, 2),
        Instruction(Instruction.Type.POSITION, 3),
        Instruction(Instruction.Type.LABEL, 4)
    ]

    run_test("test_synthetic_2", stages, solutions)

def test_synthetic_fail(capsys):

        stages = [
            Stage(1, 3, [3, 1, 2, 4]),
            Stage(2, 1, [1, 2, 4, 3]),
            Stage(3, 2, [2, 3, 4, 1]),
            Stage(4, 4, [4, 3, 1, 2]),
            Stage(5, 2, [3, 2, 4, 1])
        ]

        solutions = [
            Instruction(Instruction.Type.POSITION, 3),
            Instruction(Instruction.Type.LABEL, 4),
            Instruction(Instruction.Type.LABEL, 2),
            Instruction(Instruction.Type.POSITION, 3),
            Instruction(Instruction.Type.LABEL, 2)
        ]

        assertWasThrown = False
        try:
            run_test("test_synthetic_fail", stages, solutions)
        except AssertionError as e:
            assertWasThrown = True
        finally:
            assert assertWasThrown


def run_test(testname, stages, solutions):

    solver = Memory()

    for i in range(5):
        try:
            stage = stages[i]
            given_instruction = solver.stageSolution(stage)
            expected_instruction = solutions[i]
            assert given_instruction == expected_instruction
        except AssertionError as e:
            e.args += ("Memory", testname, "Failed at Stage " + str(stage.num) + " (" + str(stage.display) + ", " + str(stage.labels) + ")",
                "Given: (" + str(given_instruction.type) + ", " + str(given_instruction.value) + ")",
                "Expecting: (" + str(expected_instruction.type) + ", " + str(expected_instruction.value) + ")",
                "Label history: " + str(solver.stageLabelHistory),
                "Position history: " + str(solver.stagePositionHistory))
            raise
