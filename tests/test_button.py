import pytest
from modules.logic.button import Button, Indicator

module = 'Button'

# Field tests are taken from real KTANE gameplay
# Synthetic tests are there to shore up missing code coverage

car_indicator = Indicator(True, 'CAR')
frk_indicator = Indicator(True, 'FRK')
off_indicator = Indicator(False, 'CAR')

def test_indicator():
    button = Button(0, car_indicator, Button.Colour.BLUE, 'Detonate')
    assert button.isIndicator(True, 'CAR')
    assert not button.isIndicator(True, 'FRK')
    assert not button.isIndicator(False, 'CAR')

def test_no_indicator():
    button = Button(5, None, Button.Colour.RED, 'Hold')
    assert not button.isIndicator(True, 'CAR')
    assert not button.isIndicator(False, 'CAR')

def test_rule_1_hold_blue():
    holdFunc = Button(5, off_indicator, Button.Colour.BLUE, "Abort").getPressAction()
    assert holdFunc != None

    releaseNumber = holdFunc(Button.Colour.BLUE)
    assert releaseNumber == 4

def test_rule_2():
    holdFunc = Button(2, off_indicator, Button.Colour.BLACK, 'Detonate').getPressAction()
    assert holdFunc == None

def test_rule_3_hold_yellow():
    holdFunc = Button(1, car_indicator, Button.Colour.WHITE, 'Press').getPressAction()
    assert holdFunc != None

    releaseNumber = holdFunc(Button.Colour.YELLOW)
    assert releaseNumber == 5

def test_rule_4():
    holdFunc = Button(3, frk_indicator, Button.Colour.RED, 'Abort').getPressAction()
    assert holdFunc == None

def test_rule_5_hold_white():
    holdFunc = Button(4, off_indicator, Button.Colour.YELLOW, 'Press').getPressAction()
    assert holdFunc != None

    releaseNumber = holdFunc(Button.Colour.WHITE)
    assert releaseNumber == 1

def test_rule_6():
    holdFunc = Button(4, off_indicator, Button.Colour.RED, 'Hold').getPressAction()
    assert holdFunc == None

def test_rule_7_hold_red():
    holdFunc = Button(0, off_indicator, Button.Colour.BLUE, 'Detonate').getPressAction()
    assert holdFunc != None

    releaseNumber = holdFunc(Button.Colour.RED)
    assert releaseNumber == 1
