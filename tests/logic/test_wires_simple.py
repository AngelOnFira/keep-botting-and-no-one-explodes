import pytest
from modules.logic.wires_simple import WiresSimple
from modules.bomb import Bomb

module = 'Simple Wires'


@pytest.fixture
def bombs():
    class Bombs:
        pass

    bomb_options = Bombs()

    even_bomb = Bomb()
    even_bomb.serial = 'ABC246'
    bomb_options.even_bomb = even_bomb

    odd_bomb = Bomb()
    odd_bomb.serial = 'ABC123'
    bomb_options.odd_bomb = odd_bomb

    return bomb_options


def test_3_wires(bombs):
    first_condition = run_test([
        'blue',
        'blue',
        'blue',
        '',
        '',
        '',
    ], bombs.even_bomb)

    assert first_condition == 2

    second_condition = run_test([
        'blue',
        '',
        'red',
        '',
        'white',
        '',
    ], bombs.even_bomb)

    assert second_condition == 5

    third_condition = run_test([
        'blue',
        '',
        'blue',
        'red',
        '',
        '',
    ], bombs.even_bomb)

    assert third_condition == 3

    fourth_condition = run_test([
        'blue',
        'red',
        '',
        '',
        'black',
        '',
    ], bombs.even_bomb)

    assert fourth_condition == 5

    mixed_condition = run_test([
        'blue',
        'white',
        '',
        'red',
        '',
        '',
    ], bombs.even_bomb)

    assert mixed_condition == 4


def test_4_wires(bombs):
    first_condition = run_test([
        'blue',
        'red',
        '',
        '',
        'red',
        'black',
    ], bombs.odd_bomb)

    assert first_condition == 5

    second_condition = run_test([
        '',
        'blue',
        'black',
        'blue',
        'yellow',
        '',
    ], bombs.odd_bomb)

    assert second_condition == 2

    third_condition = run_test([
        'black',
        '',
        'blue',
        'red',
        'yellow',
        '',
    ], bombs.even_bomb)

    assert third_condition == 1

    fourth_condition = run_test([
        'black',
        '',
        'yellow',
        'yellow',
        '',
        'red',
    ], bombs.even_bomb)

    assert fourth_condition == 6

    fifth_condition = run_test([
        'black',
        '',
        'black',
        'red',
        'yellow',
        '',
    ], bombs.odd_bomb)

    assert fifth_condition == 3


def test_5_wires(bombs):
    first_condition = run_test([
        'blue',
        'red',
        'blue',
        '',
        'red',
        'black',
    ], bombs.odd_bomb)

    assert first_condition == 5

    second_condition = run_test([
        '',
        'blue',
        'yellow',
        'red',
        'black',
        'yellow',
    ], bombs.odd_bomb)

    assert second_condition == 2

    third_condition = run_test([
        '',
        'blue',
        'yellow',
        'blue',
        'blue',
        'yellow',
    ], bombs.odd_bomb)

    assert third_condition == 3

    fourth_condition = run_test([
        'blue',
        '',
        'black',
        'red',
        'black',
        'yellow',
    ], bombs.even_bomb)

    assert fourth_condition == 1


def test_6_wires(bombs):
    first_condition = run_test([
        'blue',
        'red',
        'blue',
        'red',
        'red',
        'black',
    ], bombs.odd_bomb)

    assert first_condition == 3

    second_condition = run_test([
        'white',
        'white',
        'blue',
        'yellow',
        'red',
        'black',
    ], bombs.odd_bomb)

    assert second_condition == 4

    third_condition = run_test([
        'blue',
        'black',
        'blue',
        'yellow',
        'yellow',
        'black',
    ], bombs.odd_bomb)

    assert third_condition == 6

    fourth_condition = run_test([
        'blue',
        'red',
        'yellow',
        'red',
        'red',
        'black',
    ], bombs.odd_bomb)

    assert fourth_condition == 4


def run_test(wiresOnModule, bomb):
    wires_simple = WiresSimple()

    return wires_simple.solution(wiresOnModule, bomb)
