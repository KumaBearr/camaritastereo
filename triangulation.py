import sys
import cv2
import numpy as np
import time


def find_depth(right_point, left_point, frame_right, frame_left, baseline,f, alpha):

    # se convierte la distancia focal f de [mm] a [pixel]:
    height_right, width_right, depth_right = frame_right.shape
    height_left, width_left, depth_left = frame_left.shape

    if width_right == width_left:
        f_pixel = (width_right * 0.5) / np.tan(alpha * 0.5 * np.pi/180)

    else:
        print('Los fotogramas de la cámara izquierda y derecha no tienen la misma cantidad de píxel')

    x_right = right_point[0]
    x_left = left_point[0]

    # calcula la disparidad:
    disparity = x_left-x_right      #Desplazamiento entre fotogramas izquierdo y derecho [píxeles]

    # CALCULATE DEPTH z:
    zDepth = (baseline*f_pixel)/disparity             #profundidad en [cm]

    return zDepth
