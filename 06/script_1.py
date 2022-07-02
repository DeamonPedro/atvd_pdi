import cv2

img = cv2.imread('../assets/images/source_02.png')
(h, w) = img.shape[:2]

pivot = (w / 2, h / 2)
angle = 0


def rotate():
    global pivot
    global angle
    angle += 10
    matrix = cv2.getRotationMatrix2D(pivot, angle, 1)
    matrix = cv2.warpAffine(img, matrix, (w, h))
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
