import math

xc, yc = (640, 240)


def la_funcion(xyL: type = tuple, xyR: type = tuple):
    cuadrante = int()

    x = xyL[0] + xyR[0]
    y = (xyL[1] + xyR[1]) / 2

    x = x - xc
    y = y - yc

    m = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

    if x >= 0 >= y:
        cuadrante = 1
    elif x >= 0 <= y:
        cuadrante = 2
    elif x <= 0 <= y:
        cuadrante = 3
    elif x <= 0 >= y:
        cuadrante = 4

    return (round(x, 2), round(y,2)), round(m, 2), cuadrante


