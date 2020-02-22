# Not to be used in pytest presently.
# I am having issues with my programming environment that
# is preventing tesseract from being loaded by pytest

#import pytest
#import modules.feature_detection.memory as memory
import memory
import cv2 as cv
import os

#module = 'Memory'

def test1():
	img = cv.imread('./memory.png')
	d, b = memory.extract_text(img, '1')
	print("Display: " + d)
	print("Buttons: " + b)
	return d == '1' and b == '3124'

def test2():
	img = cv.imread('./2_mod.png')
	d, b = memory.extract_text(img, '2')
	print("Display: " + d)
	print("Buttons: " + b)
	return d == '2' and b == '2413'
	
def test3():
	img = cv.imread('./3_mod.png')
	d, b = memory.extract_text(img, '3')
	print("Display: " + d)
	print("Buttons: " + b)
	return d == '3' and b == '4213'
	
def get2and4():
	img = cv.imread('./2.png')
	memory.extract_text(img)
	img = cv.imread('./4.png')
	memory.extract_text(img)

#get2and4()
one = test1()
two = test2()
three = test3()

assert one and two and three
