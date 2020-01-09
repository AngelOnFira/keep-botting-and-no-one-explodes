from modules.simple-wires import SimpleWires
import pytest


def test_3_wires(capsys):
    first_condition = new SimpleWires([
        'blue',
        'blue',
        'blue',
        '',
        '',
        '',
    ], (0, 0))
    first_condition.solution()

    captured = capsys.readouterr()
    assert captured.out == "Simple Wires: I cut wire 2 in position 2\n"

    second_condition = new SimpleWires([
        'blue',
        '',
        'red',
        '',
        'white',
        '',
    ], (0, 0))
    second_condition.solution()

    captured = capsys.readouterr()
    assert captured.out == "Simple Wires: I cut wire 3 in position 6\n"

    third_condition = new SimpleWires([
        'blue',
        'red',
        '',
        'blue',
        '',
        '',
    ], (0, 0))
    third_condition.solution()

    captured = capsys.readouterr()
    assert captured.out == "Simple Wires: I cut wire 3 in position 4\n"

    fourth_condition = new SimpleWires([
        'blue',
        'red',
        '',
        '',
        'black',
        '',
    ], (0, 0))
    fourth_condition.solution()

    captured = capsys.readouterr()
    assert captured.out == "Simple Wires: I cut wire 3 in position 5\n"

    mixed_condition = new SimpleWires([
        'blue',
        'blue',
        'white',
        '',
        'black',
        'blue',
    ], (0, 0))
    mixed_condition.solution()

    captured = capsys.readouterr()
    assert captured.out == "Simple Wires: I cut wire 4 in position 5\n"


def test_4_wires():
    first_condition = new SimpleWires([
        'blue',
        'red',
        '',
        '',
        'black',
        '',
    ], (0, 0))
    first_condition.solution()

    captured = capsys.readouterr()
    assert captured.out == "Simple Wires: I cut wire 3 in position 5\n"
