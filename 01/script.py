from random import randint
import cv2

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
COLORS = [BLUE, GREEN, RED, BLACK, GRAY]

capture = cv2.VideoCapture('../source.mp4')
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'MPEG')
output = cv2.VideoWriter('output.avi', fourcc, int(
    fps), (int(frame_width), int(frame_height)))


def draw_point(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        c = randint(0, len(COLORS)-1)
        points.append(Point(x, y, COLORS[c]))


def repaint_points():
    for item in points:
        while True:
            new_color = COLORS[randint(0, len(COLORS)-1)]
            if new_color != item.color:
                item.color = new_color
                break


def clear_points():
    points.clear()


class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


points = []

while capture.isOpened():
    ret, frame = capture.read()
    if ret is True:

        for point in points:
            cv2.circle(frame, (point.x, point.y), 3, point.color, -1)

        cv2.imshow('video', frame)
        cv2.namedWindow('video')
        cv2.setMouseCallback('video', draw_point)

        options = {
            # Space key
            32: clear_points,
            # C key
            99: repaint_points
        }

        pressed_key = cv2.waitKey(20)
        if pressed_key in options.keys():
            options.get(pressed_key)()

        output.write(frame)
    else:
        break

capture.release()
output.release()
cv2.destroyAllWindows()
