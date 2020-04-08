import cv2
import sys
sys.path.append('../modules/feature_detection')
import button

MODULE_IMAGES_DIR = "../images/modules/feature_detection/button/"


### LARGE RESOLUTION TESTS ####
def test_strip_blue_largeres():
	img = cv2.imread(MODULE_IMAGES_DIR + 'LargeRes-Red-Press-Blue-Strip.png')

	print("Testing large resolution blue strip...")
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "BLUE"

	print("Testing large resolution red button...")
	button_colour = button.extractButtonColour(img)
	assert button_colour == "RED"

def test_strip_white_largeres():
	img = cv2.imread(MODULE_IMAGES_DIR + 'LargeRes-Red-Press-White-Strip.png')

	print("Testing large resolution white strip...")
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "WHITE"

	print("Testing large resolution red button...")
	button_colour = button.extractButtonColour(img)
	assert button_colour == "RED"

def test_strip_yellow_largeres():
	img = cv2.imread(MODULE_IMAGES_DIR + 'LargeRes-Red-Press-Yellow-Strip.png')

	print("Testing large resolution yellow strip...")
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "YELLOW"

	print("Testing large resolution red button...")
	button_colour = button.extractButtonColour(img)
	assert button_colour == "RED"

def test_strip_red_largeres():
	img = cv2.imread(MODULE_IMAGES_DIR + 'LargeRes-Blue-Detonate-Red-Strip.png')

	print("Testing large resolution red strip...")
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "RED"

	print("Testing large resolution blue button...")
	button_colour = button.extractButtonColour(img)
	assert button_colour == "BLUE"

def test_strip_black_largres():
	img = cv2.imread(MODULE_IMAGES_DIR + 'Yellow-Hold-Black-Strip.png')

	print("Testing large resolution black strip...")
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "UNKNOWN"

	print("Testing large resolution yellow button...")
	button_colour = button.extractButtonColour(img)
	assert button_colour == "YELLOW"


### SMALL RESOLUTION TESTS ###
def test_strip_blue_smallres():
	img = cv2.imread(MODULE_IMAGES_DIR + 'SmallRes-Red-Abort-Blue-Strip.png')

	print("Testing small resolution blue strip...")
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "BLUE"

	print("Testing small resolution red button...")
	button_colour = button.extractButtonColour(img)
	assert button_colour == "RED"

def test_strip_white_smallres():
	img = cv2.imread(MODULE_IMAGES_DIR + 'SmallRes-Red-Abort-White-Strip.png')

	print("Testing small resolution white strip...")
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "WHITE"

	print("Testing small resolution red button...")
	button_colour = button.extractButtonColour(img)
	assert button_colour == "RED"

def test_strip_yellow_smallres():
	img = cv2.imread(MODULE_IMAGES_DIR + 'SmallRes-Red-Abort-Yellow-Strip.png')

	print("Testing small resolution yellow strip...")
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "YELLOW"

	print("Testing small resolution red button...")
	button_colour = button.extractButtonColour(img)
	assert button_colour == "RED"

def test_strip_red_smallres():
	img = cv2.imread(MODULE_IMAGES_DIR + 'SmallRes-Red-Abort-Red-Strip.png')

	print("Testing small resolution red strip...")
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "RED"

	print("Testing small resolution red button...")
	button_colour = button.extractButtonColour(img)
	assert button_colour == "RED"


### DARKER SHADES TESTS ###
def test_strip_darkblue_largeres():
	img = cv2.imread(MODULE_IMAGES_DIR + 'Blue-Abort-DarkBlue-Strip.png')

	print("Testing dark blue strip...")
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "BLUE"

	print("Testing blue button...")
	button_colour = button.extractButtonColour(img)
	assert button_colour == "BLUE"

def test_strip_darkwhite_largeres():
	img = cv2.imread(MODULE_IMAGES_DIR + 'White-Detonate-Grey-Strip.png')

	print("Testing dark white strip...")
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "WHITE"

	print("Testing white button...")
	button_colour = button.extractButtonColour(img)
	assert button_colour == "WHITE"

def test_strip_darkyellow_largeres():
	img = cv2.imread(MODULE_IMAGES_DIR + 'Red-Detonate-DarkYellow-Strip.png')

	print("Testing dark yellow strip...")
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "YELLOW"

	print("Testing red button...")
	button_colour = button.extractButtonColour(img)
	assert button_colour == "RED"

def test_strip_darkred_largeres():
	img = cv2.imread(MODULE_IMAGES_DIR + 'Blue-Abort-DarkRed-Strip.png')

	print("Testing dark red strip...")
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "RED"

	print("Testing blue button...")
	button_colour = button.extractButtonColour(img)
	assert button_colour == "BLUE"


test_strip_blue_largeres()
test_strip_white_largeres()
test_strip_yellow_largeres()
test_strip_red_largeres()
test_strip_black_largres()

test_strip_blue_smallres()
test_strip_white_smallres()
test_strip_yellow_smallres()
test_strip_red_smallres()

test_strip_darkblue_largeres()
test_strip_darkwhite_largeres()
test_strip_darkyellow_largeres()
test_strip_darkred_largeres()