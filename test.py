import os

os.environ['DISPLAY'] = ':0'
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pyautogui

img1 = cv2.imread('bomb.png',0)

image = pyautogui.screenshot()
img2=cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
plt.imshow(img3)
plt.show()
cv2.imwrite("tes.png", img3)