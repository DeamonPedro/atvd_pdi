# coding=utf-8
from math import*
from typing import Tuple

from cv2 import Mat
from lib.face_analyzer import FaceAnalyzer
import cv2

face_cascade = cv2.CascadeClassifier(
    '../assets/classifiers/haarcascade_frontalface_alt.xml')
capture = cv2.VideoCapture('../assets/videos/source_02.mp4')


def demarcate_face(mat: Mat, face_bounds: Tuple[int, int, int, int], face_label: str) -> None:
    (x, y, w, h) = face_bounds
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.4
    font_thickness = 1
    text_color = (255, 255, 255)
    text_padding = 6
    frame_bg_color = (0, 0, 0)
    frame_thickness = 2
    cv2.rectangle(mat, (x, y), (x+w, y+h), frame_bg_color, frame_thickness)
    (text_w, text_h), _ = cv2.getTextSize(
        face_label,
        font,
        font_scale,
        font_thickness)
    cv2.rectangle(
        mat,
        (x - int(frame_thickness / 2), y + h),
        (x + text_w + 2 * text_padding,
         y + h + text_h + 2 * text_padding),
        frame_bg_color, -1)
    cv2.putText(
        frame,
        face_label,
        (x + text_padding - int(font_thickness/2), y + h + text_h + text_padding),
        font,
        font_scale,
        text_color,
        font_thickness,
        cv2.LINE_AA)


face_analyzer = FaceAnalyzer(min_similarity=0.8, face_bank_len=30)

while capture.isOpened():
    ret, frame = capture.read()
    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 6, minSize=(100, 100))
        for (x, y, w, h) in faces:
            face_id, similarity = face_analyzer.identify_face(
                frame[y:y+h, x:x+w])
            demarcate_face(frame, (x, y, w, h),
                           f'ID: {face_id} | SIM {round(similarity, 2)}')
        options = {
            ord('q'): lambda: capture.release()
        }
        pressed_key = cv2.waitKey(10)
        if pressed_key in options.keys():
            options.get(pressed_key)()

        cv2.imshow('video', frame)
    else:
        break

print(len(face_analyzer.identified_faces))

capture.release()
cv2.destroyAllWindows()
