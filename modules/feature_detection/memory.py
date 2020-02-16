import cv2 as cv
import pytesseract
import numpy as np

# can this be removed?
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

class ColourRange:

	def __init__(self, min, max):
		self.min = np.array(min, np.uint8)
		self.max = np.array(max, np.uint8)	

WHITE = ColourRange([0,0,215], [10,40,255])
BROWN = ColourRange([15,50,20], [25,200,50])

# as provided by opencv-python's documentation
def harrisCorner(img):
	gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

	# find Harris corners
	gray = np.float32(gray)
	dst = cv.cornerHarris(gray,2,3,0.04)
	dst = cv.dilate(dst,None)
	ret, dst = cv.threshold(dst,0.01*dst.max(),255,0)
	dst = np.uint8(dst)

	# find centroids
	ret, labels, stats, centroids = cv.connectedComponentsWithStats(dst)

	# define the criteria to stop and refine the corners
	criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
	corners = cv.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

	# Now draw them
	res = np.hstack((centroids,corners))
	res = np.int0(res)
	img[res[:,1],res[:,0]]=[0,0,255]
	img[res[:,3],res[:,2]] = [0,255,0]
	
	cv.imshow('harris', img)
	return img

def extract_text_helper(img, hsv, c_range):
	mask = cv.inRange(hsv, c_range.min, c_range.max)
	img = cv.bitwise_and(img, img, mask=mask)
	cv.imshow('mask', mask)
	cv.imshow('features', img)
	cv.waitKey(0)
	return pytesseract.image_to_string(img)
	
def extract_text(img):
	img = harrisCorner(img) # odd, but it currently only seems to register the buttons after applying Harris Corner
	hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
	display_text = extract_text_helper(img, hsv_img, WHITE)
	buttons_text = extract_text_helper(img, hsv_img, BROWN)
	return (display_text, buttons_text)