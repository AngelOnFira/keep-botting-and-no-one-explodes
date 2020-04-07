import cv2
import sys
sys.path.append('../modules/feature_detection')
import button

MODULE_IMAGES_DIR = "../images/modules/feature_detection/button/"


### LARGE RESOLUTION TESTS ####
def test_strip_blue_largeres():
	print("Testing blue strip...")
	img = cv2.imread(MODULE_IMAGES_DIR + 'Press-Red-Blue-Strip.png')
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "BLUE"

def test_strip_white_largeres():
	print("Testing white strip...")
	img = cv2.imread(MODULE_IMAGES_DIR + 'Press-Red-White-Strip.png')
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "WHITE"

def test_strip_yellow_largeres():
	print("Testing yellow strip...")
	img = cv2.imread(MODULE_IMAGES_DIR + 'Press-Red-Yellow-Strip.png')
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "YELLOW"

def test_strip_other_largeres():
	print("Testing other strip...")
	img = cv2.imread(MODULE_IMAGES_DIR + 'Detonate-Blue-Red-Strip.png')
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "OTHER"


### SMALL RESOLUTION TESTS ###
def test_strip_blue_smallres():
	print("Testing blue strip...")
	img = cv2.imread(MODULE_IMAGES_DIR + 'SmallRes-Abort-Red-Blue-Strip.png')
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "BLUE"

def test_strip_white_smallres():
	print("Testing white strip...")
	img = cv2.imread(MODULE_IMAGES_DIR + 'SmallRes-Abort-Red-White-Strip.png')
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "WHITE"

def test_strip_yellow_smallres():
	print("Testing yellow strip...")
	img = cv2.imread(MODULE_IMAGES_DIR + 'SmallRes-Abort-Red-Yellow-Strip.png')
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "YELLOW"

def test_strip_other_smallres():
	print("Testing other strip...")
	img = cv2.imread(MODULE_IMAGES_DIR + 'SmallRes-Abort-Red-Red-Strip.png')
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "OTHER"


### DARKER SHADES TESTS ###
def test_strip_darkblue_largeres():
	print("Testing dark blue strip...")
	img = cv2.imread(MODULE_IMAGES_DIR + 'Blue-Abort-DarkBlue-Strip.png')
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "BLUE"

def test_strip_darkwhite_largeres():
	print("Testing dark white strip...")
	img = cv2.imread(MODULE_IMAGES_DIR + 'Detonate-White-Grey-Strip.png')
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "WHITE"

def test_strip_darkyellow_largeres():
	print("Testing dark yellow strip...")
	img = cv2.imread(MODULE_IMAGES_DIR + 'Red-Detonate-DarkYellow-Strip.png')
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "YELLOW"

def test_strip_darkother_largeres():
	print("Testing dark other strip...")
	img = cv2.imread(MODULE_IMAGES_DIR + 'Blue-Abort-DarkRed-Strip.png')
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "OTHER"


test_strip_blue_largeres()
test_strip_white_largeres()
test_strip_yellow_largeres()
test_strip_other_largeres()

test_strip_blue_smallres()
test_strip_white_smallres()
test_strip_yellow_smallres()
test_strip_other_smallres()

test_strip_darkblue_largeres()
test_strip_darkwhite_largeres()
test_strip_darkyellow_largeres()
test_strip_darkother_largeres()