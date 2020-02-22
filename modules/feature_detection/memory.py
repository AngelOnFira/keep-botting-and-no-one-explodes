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
BROWN = ColourRange([15,65,38], [25,83,55])

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

def extract_text_helper(img, hsv, c_range, img_out=None):
	mask = cv.inRange(hsv, c_range.min, c_range.max)
	#img = cv.medianBlur(img,5)
	#img = cv.GaussianBlur(img, (5, 5), 0)
	img = cv.bitwise_and(img, img, mask=mask)
	#img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	#img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
	img = cv.bitwise_not(img)
	#img = cv.GaussianBlur(img, (5, 5), 0)
	#img = cv.blur(img, (5, 5))

	if img_out is not None:
		cv.imwrite(img_out + '_mask.png', mask)
		cv.imwrite(img_out + '_feats.png', img)
	return pytesseract.image_to_string(img)
	
def extract_text(img, img_out=None):
	#img = harrisCorner(img) # odd, but it currently only seems to register the buttons after applying Harris Corner
	hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
	if img_out is not None:
		img_out += '_display'
	display_text = extract_text_helper(img, hsv_img, WHITE, img_out)
	if img_out is not None:
		img_out += '_buttons'
	buttons_text = extract_text_helper(img, hsv_img, BROWN, img_out)
	return (display_text, buttons_text)