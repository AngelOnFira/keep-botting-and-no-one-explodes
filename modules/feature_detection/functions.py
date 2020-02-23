import pyautogui
import cv2
import numpy as np


def takeScreenshot():
    image = pyautogui.screenshot()
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)


def matchImages(img1, img2, numPoints):
    # TODO when loading images, throw out
    # any points that arent in ideal place

    orb = cv2.ORB_create()

    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(des1, des2)
    print(matches[0])
    matches = sorted(matches, key=lambda x: x.distance)

    numPoints = min(numPoints, len(matches))

    # src_pts = np.float32([kp1[m.queryIdx].pt for m in range(10)]).reshape(-1, 1, 2)
    dst_pts = np.float32(
        [kp2[matches[i].trainIdx].pt for i in range(numPoints)]).reshape(-1, 1, 2)

    return dst_pts
