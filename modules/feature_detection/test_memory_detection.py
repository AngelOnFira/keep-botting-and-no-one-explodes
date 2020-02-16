# Not to be used in pytest presently.
# I am having issues with my programming environment that
# is preventing tesseract from being loaded by pytest

#import pytest
#import modules.feature_detection.memory as memory
import memory
import cv2 as cv
import os

#module = 'Memory'

def test():
	print("cwd: \n\t" + str(os.getcwd()))
	img = cv.imread('./memory.png')
	d, b = memory.extract_text(img)
	print("Display: " + d)
	print("Buttons: " + b)
	assert d == '1' and b == '3124'
	
test()