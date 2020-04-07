import cv2
import modules.feature_detection.button as button

MODULE_IMAGES_DIR = "../images/modules/feature_detection/button/"

def test_strip_blue():
	print("Testing blue strip...")
	img = cv2.imread(MODULE_IMAGES_DIR + 'Press-Red-Blue-Strip.png')
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "BLUE"

def test_strip_white():
	print("Testing white strip...")
	img = cv2.imread(MODULE_IMAGES_DIR + 'Press-Red-White-Strip.png')
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "WHITE"

def test_strip_yellow():
	print("Testing yellow strip...")
	img = cv2.imread(MODULE_IMAGES_DIR + 'Press-Red-Yellow-Strip.png')
	strip_colour = button.extractStripColour(img)
	assert strip_colour == "YELLOW"

test_strip_blue()
test_strip_white()
test_strip_yellow()