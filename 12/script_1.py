import cv2

capture = cv2.VideoCapture('video.mp4')


while capture.isOpened():
    ret, frame = capture.read()
    if ret is True:
        edges = cv2.Canny(frame, 100, 200)
        cv2.imshow('video', edges)
        cv2.namedWindow('video')

        options = {
            ord('q'): lambda: capture.release()
        }
        pressed_key = cv2.waitKey(20)
        if pressed_key in options.keys():
            options.get(pressed_key)()
    else:
        break

capture.release()
cv2.destroyAllWindows()
