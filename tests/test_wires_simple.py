import pytest
from modules.wires_simple import WiresSimple


def test_3_wires(capsys):
    first_condition = WiresSimple((0, 0), "ABC123")
    first_condition.solution([
        'blue',
        'blue',
        'blue',
        '',
        '',
        '',
    ])

    captured = capsys.readouterr()
    assert captured.out == "Simple Wires: I cut wire 2 in position 2\n"

    second_condition = WiresSimple((0, 0), "ABC123")
    second_condition.solution([
        'blue',
        '',
        'red',
        '',
        'white',
        '',
    ])

    captured = capsys.readouterr()
    assert captured.out == "Simple Wires: I cut wire 3 in position 6\n"

    third_condition = WiresSimple((0, 0), "ABC123")
    third_condition.solution([
        'blue',
        'red',
        '',
        'blue',
        '',
        '',
    ])

    captured = capsys.readouterr()
    assert captured.out == "Simple Wires: I cut wire 3 in position 4\n"

    fourth_condition = WiresSimple((0, 0), "ABC123")
    fourth_condition.solution([
        'blue',
        'red',
        '',
        '',
        'black',
        '',
    ])

    captured = capsys.readouterr()
    assert captured.out == "Simple Wires: I cut wire 3 in position 5\n"

    mixed_condition = WiresSimple((0, 0), "ABC123")
    mixed_condition.solution([
        'blue',
        'blue',
        'white',
        '',
        'black',
        'blue',
    ])

    captured = capsys.readouterr()
    assert captured.out == "Simple Wires: I cut wire 4 in position 5\n"


def test_4_wires(capsys):
    first_condition = WiresSimple((0, 0), "ABC123")
    first_condition.solution([
        'blue',
        'red',
        '',
        '',
        'black',
        '',
    ])

    captured = capsys.readouterr()
    assert captured.out == "Simple Wires: I cut wire 3 in position 5\n"
