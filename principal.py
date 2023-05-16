########## UwU ########
import numpy as np
import cv2
import shape_recognition as shape
import triangulation as tri
import webam as hsv
import ffuncion as ff
print("librerias leidas")

########## enciende camara y se pone resolucion/fps y datos de importancia ########
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 120)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

B = 8.5  # distancia entre los lentes
f = 2.4  # distancia focal
alpha = 62.5  # grados en horinzontal de cada camara`


######## se lee camara y se divide en 2 ########
height = 480
width = 1280
# print(width)
# print(height)

while (1):
    s, frame = cap.read()
    left = frame[0:height, 0:int(width / 2)]
    right = frame[0:height, int(width / 2):(width)]

    ######## aplicacion de filtro de color ########
    mask_right = hsv.add_HSV_filter(right, 1)
    mask_left = hsv.add_HSV_filter(left, 0)
    res_right = cv2.bitwise_and(right, right, mask=mask_right)
    res_left = cv2.bitwise_and(left, left, mask=mask_left)

    ########## en busca del la pelota ########
    circles_right, xyr = shape.find_circles(right, mask_right)
    circles_left, xyl = shape.find_circles(left, mask_left)
    cv2.circle(frame, (640, 240), 2, (255, 255, 0), 2)

    if np.all(circles_right) == None or np.all(circles_left) == None:
        cv2.putText(right, "no hay nada", (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText(left, "no hay nada", (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    else:
        # Función para calcular la profundidad del objeto. Salidas vectoriales de todas las profundidades en caso de varias bolas.
        depth = tri.find_depth(circles_right, circles_left, right, left, B, f, alpha)
        posicion, magnitud, cuadrante = ff.la_funcion(xyl, xyr)
        """if magnitud <= 50:
            if cuadrante == 1 :
                UNO_depth = depth * 1
                print("depth =", UNO_depth)
            elif cuadrante == 2:
                DOS_depth = depth * 1
                print("depth =", DOS_depth)
            elif cuadrante == 3:
                TRE_depth = depth * 1
                print("depth =", TRE_depth)
            elif cuadrante == 4:
                CUA_depth = depth * 1
                print("depth =", CUA_depth)
        elif magnitud >=51<= 100 :
            if cuadrante == 1 :
                UNO1_depth = depth * 1
                print("depth =", UNO1_depth)
            elif cuadrante == 2:
                DOS1_depth = depth * 1
                print("depth =", DOS1_depth)
            elif cuadrante == 3:
                TRE1_depth = depth * 1
                print("depth =", TRE1_depth)
            elif cuadrante == 4:
                CUA1_depth = depth * 1
                print("depth =", CUA1_depth)
        elif magnitud >=101<= 150 :
            if cuadrante == 1 :
                UNO2_depth = depth * 1
                print("depth =", UNO2_depth)
            elif cuadrante == 2:
                DOS2_depth = depth * 1
                print("depth =", DOS2_depth)
            elif cuadrante == 3:
                TRE2_depth = depth * 1
                print("depth =", TRE2_depth)
            elif cuadrante == 4:
                CUA2_depth = depth * 1
                print("depth =", CUA2_depth)
        elif magnitud >=151<= 200 :
            if cuadrante == 1 :
                UNO4_depth = depth * 1
                print("depth =", UNO4_depth)
            elif cuadrante == 2:
                DOS4_depth = depth * 1
                print("depth =", DOS4_depth)
            elif cuadrante == 3:
                TRE4_depth = depth * 1
                print("depth =", TRE4_depth)
            elif cuadrante == 4:
                CUA4_depth = depth * 1
                print("depth =", CUA4_depth)
        elif magnitud >=201<= 250 :
            if cuadrante == 1 :
                UNO4_depth = depth * 1
                print("depth =", UNO4_depth)
            elif cuadrante == 2:
                DOS4_depth = depth * 1
                print("depth =", DOS4_depth)
            elif cuadrante == 3:
                TRE4_depth = depth * 1
                print("depth =", TRE4_depth)
            elif cuadrante == 4:
                CUA4_depth = depth * 1
                print("depth =", CUA4_depth)"""



        cv2.putText(right, "shi hay algo", (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (124, 252, 0), 2)
        cv2.putText(left, "shi hay algo", (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (124, 252, 0), 2)

        ########## saca calculacion ########

        cv2.putText(right, "la distancia es de: " + str(round(depth, 3)), (200, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (124, 252, 0),
                    2)
        cv2.putText(left, "la distancia es de: " + str(round(depth, 3)), (200, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (124, 252, 0),
                    2)

        # Multiply computer value with 205.8 to get real-life depth in [cm]. The factor was found manually.
        #print("Depth: ", depth)
        print("depth", depth)
        print("xl =", ff.la_funcion(xyl,xyr))




    cv2.imshow('left', left)
    cv2.imshow('Right', right)

    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

cap.release()
