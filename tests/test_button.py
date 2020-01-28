import pytest
from modules.logic.button import Button, Strip

module = 'Button'
strip_yellow = Strip('yellow')
strip_blue = Strip('blue')
strip_other = Strip('other')

# If the button is blue and the button says "Abort", hold the button and refer to "Releasing a Held Button".
def test_scenario_one():

    button = Button('blue', 'Abort', 'RELEASED')

    button_t1 = button.pressButton(2, 'CAR', True, strip_other, "0741") == 'RELEASED'
    button_t2 = button.pressButton(2, 'CAR', True, strip_other, "0742") == 'HELD'
    button_t3 = button.pressButton(2, 'CAR', True, strip_yellow, "0501") == 'RELEASED'
    button_t4 = button.pressButton(2, 'CAR', True, strip_yellow, "0402") == 'HELD'
    button_t5 = button.pressButton(2, 'CAR', True, strip_blue, "0034") == 'RELEASED'
    button_t6 = button.pressButton(2, 'CAR', True, strip_blue, "0515") == 'HELD'

    assert button_t1
    assert button_t2
    assert button_t3
    assert button_t4
    assert button_t5
    assert button_t6

# If there is more than 1 battery on the bomb and the button says "Detonate", press and immediately release the button.
def test_scenario_two():

    button = Button('blue', 'Detonate', 'RELEASED')

    button_t1 = button.pressButton(0, 'CAR', True, strip_other, "2345") == 'HELD'
    button_t2 = button.pressButton(1, 'CAR', True, strip_other, "0741") == 'RELEASED'
    button_t3 = button.pressButton(2, 'CAR', True, strip_other, "0741") == 'RELEASED'

    assert button_t1
    assert button_t2 
    assert button_t3

# If the button is white and there is a lit indicator with label CAR, hold the button and refer to "Releasing a Held Button".
def test_scenario_three():

    button = Button('white', 'Bomb', 'RELEASED')

    button_t1 = button.pressButton(2, 'CAR', True, strip_blue, "1233") == 'HELD'
    button_t2 = button.pressButton(2, 'CAR', True, strip_blue, "1234") == 'RELEASED'
    button_t3 = button.pressButton(2, 'CAR', True, strip_other, "0000") == 'HELD'
    button_t4 = button.pressButton(2, 'CAR', True, strip_other, "0010") == 'RELEASED'
    button_t5 = button.pressButton(2, 'CAR', True, strip_yellow, "3456") == 'RELEASED'
    button_t6 = button.pressButton(2, 'CAR', True, strip_yellow, "3466") == 'HELD'

    assert button_t1
    assert button_t2
    assert button_t3
    assert button_t4
    assert button_t5
    assert button_t6

# If there are more than 2 batteries on the bomb and there is a lit indicator with label FRK, press and immediately release the button.
def test_scenario_four():

    button = Button('blue', 'Aborttt', 'RELEASED')

    button_t1 = button.pressButton(1, 'FRK', True, strip_yellow, "0741") == 'HELD'
    button_t2 = button.pressButton(2, 'FRK', True, strip_other, "0742") == 'HELD'
    button_t3 = button.pressButton(3, 'FRK', True, strip_other, "2345") == 'RELEASED'
    button_t4 = button.pressButton(4, 'FRK', False, strip_blue, "2345") == 'RELEASED'
    button_t5 = button.pressButton(4, 'FRK', False, strip_blue, "2355") == 'HELD'

    assert button_t1
    assert button_t2
    assert button_t3
    assert button_t4
    assert button_t5   

# If the button is yellow, hold the button and refer to "Releasing a Held Button".
def test_scenario_five():

    button = Button('yellow', 'Aborttt', 'RELEASED')

    button_t1 = button.pressButton(0, 'FRK', True, strip_yellow, "0741") == 'HELD'
    button_t2 = button.pressButton(0, 'FRK', True, strip_yellow, "0751") == 'RELEASED'
    button_t3 = button.pressButton(1, 'FRK', True, strip_other, "0742") == 'HELD'
    button_t4 = button.pressButton(1, 'FRK', True, strip_other, "0741") == 'RELEASED'
    button_t5 = button.pressButton(2, 'FRK', False, strip_blue, "2345") == 'RELEASED'
    button_t6 = button.pressButton(2, 'FRK', False, strip_blue, "2356") == 'HELD'

# If the button is red and the button says "Hold", press and immediately release the button.
def test_scenario_six():

    button_one = Button('red', 'Hold', 'RELEASED')
    button_two = Button('blue', 'Hold', 'RELEASED')
    button_three = Button('red', 'Holt', 'RELEASED')

    button_one_t1 = button_one.pressButton(3, 'FRK', False, strip_yellow, "0741") == 'RELEASED'
    button_two_t1 = button_two.pressButton(3, 'FRK', False, strip_yellow, "0741") == 'HELD'
    button_three_t1 = button_three.pressButton(3, 'FRK', False, strip_blue, "0751") == 'HELD'

    assert button_one_t1
    assert button_two_t1
    assert button_three_t1

# If none of the above apply, hold the button and refer to "Releasing a Held Button".
def test_scenario_seven():

    button_one = Button('blue', 'AbOrt', 'RELEASED')
    button_two = Button('red', 'Detonate', 'RELEASED')
    button_three = Button('white', 'Hold', 'RELEASED')
    button_four = Button('white', 'Abort', 'RELEASED')
    button_five = Button('yellow', 'DetOnate', 'RELEASED')
    button_six = Button('red', 'HOld', 'RELEASED')
    button_seven = Button('black', 'Explode', 'RELEASED')

    button_one_t1 = button_one.pressButton(0, 'FRK', True, strip_blue, "0741") == 'RELEASED'
    button_two_t1 = button_two.pressButton(1, 'CAR', False, strip_other, "0751") == 'RELEASED'
    button_three_t1 = button_three.pressButton(2, 'FRK', True, strip_yellow, "0745") == 'RELEASED'
    button_four_t1 = button_four.pressButton(3, 'CAR', False, strip_blue, "0731") == 'HELD'
    button_five_t1 = button_five.pressButton(2, 'FRK', True, strip_other, "2345") == 'HELD'
    button_six_t1 = button_six.pressButton(1, 'CAR', False, strip_yellow, "7777") == 'HELD'
    button_seven_t1 = button_seven.pressButton(0, 'FRK', True, strip_blue, "0000") == 'HELD'

    assert button_one_t1
    assert button_two_t1
    assert button_three_t1
    assert button_four_t1
    assert button_five_t1
    assert button_six_t1
    assert button_seven_t1