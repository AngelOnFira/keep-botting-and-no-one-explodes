import cv2 as cv
import pytesseract
import numpy as np
from os import listdir
from os.path import isfile, join

# can this be removed?
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

DISPLAYS_DIRECTORY = "./displays"

class ColourRange:

	def __init__(self, min, max):
		self.min = np.array(min, np.uint8)
		self.max = np.array(max, np.uint8)

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
	img = cv.bitwise_and(img, img, mask=mask)
	img = cv.bitwise_not(img)

	if img_out is not None:
		cv.imwrite(img_out + '_mask.png', mask)
		cv.imwrite(img_out + '_feats.png', img)
	return pytesseract.image_to_string(img)

# borrowed from AngelOnFira's working branch
def matchImages(img1, img2, numPoints):
    # TODO when loading images, throw out
    # any points that arent in ideal place

    orb = cv.ORB_create()

    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    bf = cv.BFMatcher_create(cv.NORM_HAMMING, crossCheck=True)

    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    numPoints = min(numPoints, len(matches))

    # src_pts = np.float32([kp1[m.queryIdx].pt for m in range(10)]).reshape(-1, 1, 2)
    dst_pts = np.float32(
        [kp2[matches[i].trainIdx].pt for i in range(numPoints)]).reshape(-1, 1, 2)

    output = ([], matches[:numPoints])
    for i in range(numPoints):
        output[0].append(dst_pts[i][0])

    img3 = cv.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
    #cv.imwrite("tes.png", img3)

    return output

# borrowed from AngelOnFira's working branch
def detectDisplay(displayImg):
    # Have a module image passed in, figure out which one it is

    # Load array of images
    displayReferences = []

    for f in listdir(DISPLAYS_DIRECTORY):
        if isfile(join(DISPLAYS_DIRECTORY, f)):
            displayReferences += [cv.imread(join(DISPLAYS_DIRECTORY, f), 0)]

    # Check displayImg against each
    displayMatches = []

    for reference in displayReferences:
        # [[reference, sumDistance], ...]
        matches = matchImages(displayImg, reference, 10)
        displayMatches.append(
            (reference, sum([m.distance for m in matches[1]])))

    # Return most likely image
    return min(displayMatches, key=lambda match: match[1])[0]

def extract_text(img, img_out=None):
	#img = harrisCorner(img) # odd, but it currently only seems to register the buttons after applying Harris Corner
	hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
	#if img_out is not None:
	#	img_out += '_display'
	#display_text = extract_text_helper(img, hsv_img, WHITE, img_out)
	if img_out is not None:
		img_out += '_display.png'
		cv.imwrite(img_out, detectDisplay(img))

	# To do: replace with actual report from detectDisplay
	display_text = ""

	if img_out is not None:
		img_out += '_buttons'

	buttons_text = extract_text_helper(img, hsv_img, BROWN, img_out)

	return (display_text, buttons_text)
