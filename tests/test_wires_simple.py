import pytest
from modules.logic.wires_simple import WiresSimple
from utils import verifyCapture

module = 'Simple Wires'


def test_3_wires(capsys):
    first_condition = WiresSimple((0, 0), "ABC123")
    solution = first_condition.solution([
        'blue',
        'blue',
        'blue',
        '',
        '',
        '',
    ])

    assert solution == (2, 2,)

    second_condition = WiresSimple((0, 0), "ABC123")
    solution = second_condition.solution([
        'blue',
        '',
        'red',
        '',
        'white',
        '',
    ])

    assert solution == (3, 5,)

    third_condition = WiresSimple((0, 0), "ABC123")
    solution = third_condition.solution([
        'blue',
        '',
        'blue',
        'red',
        '',
        '',
    ])

    assert solution == (2, 3,)

    fourth_condition = WiresSimple((0, 0), "ABC123")
    solution = fourth_condition.solution([
        'blue',
        'red',
        '',
        '',
        'black',
        '',
    ])

    assert solution == (3, 5,)

    mixed_condition = WiresSimple((0, 0), "ABC123")
    solution = mixed_condition.solution([
        'blue',
        'white',
        '',
        'red',
        '',
        '',
    ])

    assert solution == (3, 4,)


def test_4_wires(capsys):
    first_condition2 = WiresSimple((0, 0), "XXXXX7")
    solution = first_condition2.solution([
        'blue',
        'red',
        '',
        '',
        'red',
        'black',
    ])

    assert solution == (3, 5,)
