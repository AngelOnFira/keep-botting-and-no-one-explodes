import cv2
from os import listdir
from os.path import isfile, join

RESIZED_IMAGE_WIDTH = 300

def extractColour(img, img_out=None):

	colour = "UNKNOWN"

	# Colour boundaries may need tweaking to improve success rate for extracting colour
	red_boundaries    = [[22, 22, 157], [64, 52, 255]]
	blue_boundaries   = [[86, 31, 4], [255, 120, 50]]
	yellow_boundaries = [[0, 150, 200], [40, 255, 255]]
	white_boundaries  = [[180, 180, 180],[255, 255, 255]]

	y = img.shape[0]
	x = img.shape[1]

	strip_colour_index0 = 0
	strip_colour_index1 = 0
	strip_colour_index2 = 0
	pixelcount = 0

	for y in range(0, y):
		for x in range(0, x):
			pixel_colour = img[y,x]
			strip_colour_index0 += pixel_colour[0]
			strip_colour_index1 += pixel_colour[1]
			strip_colour_index2 += pixel_colour[2]
			pixelcount += 1

	average_strip_colour = [round(strip_colour_index0/pixelcount), round(strip_colour_index1/pixelcount), round(strip_colour_index2/pixelcount)]
	#print(average_strip_colour) # -> Useful for debugging colour boundaries

	if extractColourHelper(average_strip_colour, white_boundaries):
		colour = "WHITE"
		return colour

	if extractColourHelper(average_strip_colour, yellow_boundaries):
		colour = "YELLOW"
		return colour

	if extractColourHelper(average_strip_colour, blue_boundaries):
		colour = "BLUE"
		return colour

	if extractColourHelper(average_strip_colour, red_boundaries):
		colour = "RED"
		return colour

	return colour

def extractColourHelper(avg_strip_color, colour_boundaries):
	if avg_strip_color[0] >= colour_boundaries[0][0] and avg_strip_color[1] >= colour_boundaries[0][1] and  avg_strip_color[2] >= colour_boundaries[0][2]:
		if avg_strip_color[0] <= colour_boundaries[1][0] and avg_strip_color[1] <= colour_boundaries[1][1] and avg_strip_color[2] <= colour_boundaries[1][2]:
			return True

def resizeImage(img, image_width, img_out=None):
	new_ratio = image_width / img.shape[1]
	new_dimensions = (image_width, int(img.shape[0] * new_ratio)) # New image height computed here
	resized_img = cv2.resize(img, new_dimensions, interpolation = cv2.INTER_AREA)
	return resized_img

def extractStripColour(img, img_out=None):
	resized_img = resizeImage(img, RESIZED_IMAGE_WIDTH)
	cropped_img = resized_img[136:256, 240:266]
	strip_colour = extractColour(cropped_img)
	return strip_colour

def extractButtonColour(img, img_out=None):
	resized_img = resizeImage(img, RESIZED_IMAGE_WIDTH)
	cropped_img = resized_img[120:140, 80:160]
	button_colour = extractColour(cropped_img)
	return button_colour