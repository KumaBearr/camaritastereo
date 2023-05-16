import sys
import cv2
import numpy as np
import time


def add_HSV_filter(frame, camera):


    blur = cv2.GaussianBlur(frame,(5,5),0)

    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    amarillo_aldrikr = np.array([12, 70, 120])
    amarillo_weror = np.array([29, 255, 255])
    amarillo_aldrikl = np.array([12, 70, 120])
    amarillo_werol = np.array([29, 255, 255])

    if(camera == 1):
        mask = cv2.inRange(hsv, amarillo_aldrikr, amarillo_weror)
    else:
        mask = cv2.inRange(hsv, amarillo_aldrikl, amarillo_werol)

    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    return mask