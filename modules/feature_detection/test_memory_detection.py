# Not to be used in pytest presently.
# I am having issues with my programming environment that
# is preventing tesseract from being loaded by pytest

import memory
import cv2 as cv
import os

def test1():
	img = cv.imread('./1_mod.png')
	d, b = memory.extract_text(img)
	print("Display: " + d)
	print("Buttons: " + b)
	return d == '1' and b == '4123'

def test2():
	img = cv.imread('./2_mod.png')
	d, b = memory.extract_text(img)
	print("Display: " + d)
	print("Buttons: " + b)
	return d == '2' and b == '2413'

def test3():
	img = cv.imread('./3_mod.png')
	d, b = memory.extract_text(img)
	print("Display: " + d)
	print("Buttons: " + b)
	return d == '3' and b == '4213'

one = test1()
two = test2()
three = test3()

assert one and two and three
