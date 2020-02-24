import pyautogui
import cv2
import numpy as np
import os
import time
from modules.controller.controller import getMousePosition


def lstAvg(lst):
    return int(sum(lst) / len(lst))


def takeScreenshot():
    # TODO change this to full screen, this
    # is only for my second monitor
    image = pyautogui.screenshot(region=(1920, 0, 1920, 1080))
    cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("screen.png", cv_image)

    return cv_image


def matchImages(img1, img2, numPoints):
    # TODO when loading images, throw out
    # any points that arent in ideal place

    orb = cv2.ORB_create()

    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    numPoints = min(numPoints, len(matches))

    # src_pts = np.float32([kp1[m.queryIdx].pt for m in range(10)]).reshape(-1, 1, 2)
    dst_pts = np.float32(
        [kp2[matches[i].trainIdx].pt for i in range(numPoints)]).reshape(-1, 1, 2)

    output = ([], matches[:numPoints])
    for i in range(numPoints):
        output[0].append(dst_pts[i][0])

    img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
    cv2.imwrite("tes.png", img3)

    return output


def averages(matches):
    x_list = []
    for point in matches:
        x_list.append(point[0])

    y_list = []
    for point in matches:
        y_list.append(point[1])

    return (lstAvg(x_list), lstAvg(y_list),)


def loadSettings():
    settings = {}
    data = []
    if os.path.exists('settings.txt'):
        data = [line.strip()
                for line in open("settings.txt", 'r')]

    for item in data:
        itemSplit = item.split("=")
        settings[itemSplit[0]] = itemSplit[1]

    return data


def getWindowPosition():
    command = "none"
    firstPos = None
    secondPos = None
    while command != "":
        print("Put your cursor at the top left of the game window. It will be recorded in 2 seconds.")
        time.sleep(2)
        firstPos = getMousePosition()

        print("Put your cursor at the bottom right of the game window. It will be recorded in 2 seconds.")
        time.sleep(2)
        secondPos = getMousePosition()

        command = input(
            'Type "repeat" if you want to rerecord the locations: ')

    output = "gameWindowLoc={},{},{},{}".format(
        firstPos[0],
        firstPos[1],
        secondPos[0],
        secondPos[1],
    )

    print(globals())
    exit()
    globals()['settings']['gameWindowLoc'] = output.split("=")[0]

    file_object = open('settings.txt', 'a')
    file_object.write(output)
    file_object.close()
