import pytest
from modules.logic.wires_complicated import WiresComplicated

module = 'Complicated Wires'

def test_white_wire(capsys):
    validator = WiresComplicated()

    solution_none = validator.solution(['white'], False, False, 2, True, "0")
    solution_star = validator.solution(['white'], True, False, 2, True, "0")
    solution_led = validator.solution(['white'], False, True, 2, True, "0")
    solution_both1 = validator.solution(['white'], True, True, 2, True, "0")
    solution_both2 = validator.solution(['white'], True, True, 1, True, "0")

    assert solution_none
    assert solution_star
    assert not solution_led
    assert solution_both1
    assert not solution_both2

def test_red_wire(capsys):
    validator = WiresComplicated()

    solution_none1 = validator.solution(['red'], False, False, 2, True, "RJ20")
    solution_none2 = validator.solution(['red'], False, False, 2, True, "FJ31")
    solution_star = validator.solution(['red'], True, False, 2, True, "0")
    solution_led1 = validator.solution(['red'], False, True, 4, True, "0")
    solution_led2 = validator.solution(['red'], False, True, 0, True, "0")
    solution_both1 = validator.solution(['red'], True, True, 2, True, "0")
    solution_both2 = validator.solution(['red'], True, True, 1, True, "0")

    assert solution_none1
    assert not solution_none2
    assert solution_star
    assert solution_led1
    assert not solution_led2
    assert solution_both1
    assert not solution_both2

def test_blue_wire(capsys):
    validator = WiresComplicated()

    solution_none1 = validator.solution(['blue'], False, False, 0, False, 'RS34')
    solution_none2 = validator.solution(['blue'], False, False, 0, False, 'RS33')
    solution_star = validator.solution(['blue'], True, False, 0, False, "0")
    solution_led1 = validator.solution(['blue'], False, True, 0, True, "0")
    solution_led2 = validator.solution(['blue'], False, True, 0, False, "0")
    solution_both1 = validator.solution(['blue'], True, True, 0, True, "0")
    solution_both2 = validator.solution(['blue'], True, True, 0, False, "0")

    assert solution_none1
    assert not solution_none2
    assert not solution_star
    assert solution_led1
    assert not solution_led2
    assert solution_both1
    assert not solution_both2

def test_both_wire(capsys):
    validator = WiresComplicated()

    solution_none1 = validator.solution(['red', 'blue'], False, False, 0, False, 'RS34')
    solution_none2 = validator.solution(['red', 'blue'], False, False, 0, False, 'RS33')
    solution_star1 = validator.solution(['red', 'blue'], True, False, 0, True, "0")
    solution_star2 = validator.solution(['red', 'blue'], True, False, 0, False, "0")
    solution_led1 = validator.solution(['red', 'blue'], False, True, 0, False, 'RS34')
    solution_led2 = validator.solution(['red', 'blue'], False, True, 0, False, 'RS33')
    solution_both = validator.solution(['red', 'blue'], True, True, 0, False, "0")
    solution_other1 = validator.solution(['red', 'white'], False, True, 0, False, "0")
    solution_other2 = validator.solution(['blue', 'white'], True, True, 2, False, "0")

    assert solution_none1
    assert not solution_none2
    assert solution_star1
    assert not solution_star2
    assert solution_led1
    assert not solution_led2
    assert not solution_both
    assert not solution_other1
    assert solution_other2