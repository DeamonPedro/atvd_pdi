from math import*
import cv2
import numpy as np

img = cv2.imread('../assets/images/source_02.png')
(h, w) = img.shape[:2]

pivot = (w / 2, h / 2)
angle = 0


def nine2one(matrix):
    return cv2.mean(matrix)[:3]


def rotation_func(img, angle, pivot):
    radian = round(radians(angle), 3)
    c = round(cos(radian), 2)
    s = round(sin(radian), 2)
    rotate_matrix = [
        [c, s],
        [-s, c]
    ]
    img_2 = np.zeros(img.shape, np.uint8)
    for y in range(w):
        for x in range(h):
            pivot_x, pivot_y = pivot
            x_, y_ = np.dot([x-pivot_x, y-pivot_y],
                            np.linalg.inv(rotate_matrix)).astype(int)
            x_, y_ = [x_+pivot_x, y_+pivot_y]
            if(x_ < 0 or y_ < 0):
                target_3x3 = np.zeros((3, 3, 3), np.uint8)
            else:
                target_3x3 = img[x_-1:x_+2, y_-1: y_+2]
            img_2[x, y] = nine2one(target_3x3)
    return img_2


def rotate():
    global pivot
    global angle
    angle += 10
    matrix = rotation_func(img, angle, pivot)
    cv2.imshow('img', matrix)


def get_mouse_position(event, x, y, flags, param):
    global pivot
    pivot = (x, y)


def finish():
    global running
    running = False


cv2.imshow('img', img)
cv2.namedWindow('img')
cv2.setMouseCallback('img', get_mouse_position)

running = True

while running:
    options = {
        # R key
        ord('r'): rotate,
        ord('q'): finish,
    }
    pressed_key = cv2.waitKey(10)
    if pressed_key in options.keys():
        options[pressed_key].__call__()

cv2.destroyAllWindows()
