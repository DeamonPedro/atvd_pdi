import torch
import cv2
import pafy
# pip install -e git+git://github.com/mohamed-challal/pafy.git@develop#egg=pafy
# sudo pip install --upgrade youtube_dl


url = "https://www.youtube.com/watch?v=nt3D26lrkho"
video = pafy.new(url)
best = video.getbest(preftype="mp4")
capture = cv2.VideoCapture(best.url)

model = torch.hub.load('ultralytics/yolov5', 'custom',
                       '../assets/trained_models/yolov5s.pt')

while capture.isOpened():
    ret, frame = capture.read()
    if ret is True:
        rows, cols, channels = frame.shape
        res = model(frame)
        for boxes in res.xyxy:
            for box in boxes:
                x1, y1, x2, y2, _, id = map(int, box.tolist())
                # car class id is 2
                if id == 2:
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

        options = {
            ord('q'): lambda: capture.release()
        }
        pressed_key = cv2.waitKey(10)
        if pressed_key in options.keys():
            options.get(pressed_key)()

        cv2.imshow('video', frame)
    else:
        break


capture.release()
cv2.destroyAllWindows()
