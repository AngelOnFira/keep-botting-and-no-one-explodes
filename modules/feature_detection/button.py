import cv2
from os import listdir
from os.path import isfile, join

def extractStripColour(img, img_out=None):

	strip_colour = "OTHER"
	r = 300.0 / img.shape[1]
	dim = (300, int(img.shape[0] * r))
	resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	cropped_img = resized_img[136:256, 240:266]

	blue_boundaries   = [[86, 31, 4], [255, 120, 50]]
	yellow_boundaries = [[0, 200, 200], [15, 255, 255]]
	white_boundaries  = [[200,200,200],[255,255,255]]

	y = cropped_img.shape[0]
	x = cropped_img.shape[1]

	strip_colour_index0 = 0
	strip_colour_index1 = 0
	strip_colour_index2 = 0
	pixelcount = 0

	for y in range(0, y):
		for x in range(0, x):
			pixel_colour = cropped_img[y,x]
			strip_colour_index0 += pixel_colour[0]
			strip_colour_index1 += pixel_colour[1]
			strip_colour_index2 += pixel_colour[2]
			pixelcount += 1

	average_strip_colour = [round(strip_colour_index0/pixelcount), round(strip_colour_index1/pixelcount), round(strip_colour_index2/pixelcount)]
	#print(average_strip_colour)

	if extractStripColourHelper(average_strip_colour, white_boundaries):
		return "WHITE"

	if extractStripColourHelper(average_strip_colour, yellow_boundaries):
		return "YELLOW"

	if extractStripColourHelper(average_strip_colour, blue_boundaries):
		return "BLUE"

	return strip_colour

def extractStripColourHelper(avg_strip_color, colour_boundaries):
	if avg_strip_color[0] >= colour_boundaries[0][0] and avg_strip_color[1] >= colour_boundaries[0][1] and  avg_strip_color[2] >= colour_boundaries[0][2]:
		if avg_strip_color[0] <= colour_boundaries[1][0] and avg_strip_color[1] <= colour_boundaries[1][1] and avg_strip_color[2] <= colour_boundaries[1][2]:
			return True
