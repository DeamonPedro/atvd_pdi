from typing import Tuple
import cv2
from cv2 import Mat


def crop_circle(img: Mat) -> Mat:
    img = img.copy()
    w, h = img.shape[:2]
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (w, h))
    img[kernel == 0] = 0
    return img


def crop_center(img: Mat, dim: Tuple[int, int]) -> Mat:
    w, h = dim
    ih, iw = img.shape[:2]
    x1 = (iw-w)//2
    y1 = (ih-h)//2
    return img[y1:y1+h, x1:x1+w].copy()


def equalize_faces(face1: Mat, face2: Mat) -> Tuple[Mat, Mat]:
    (w1, h1) = face1.shape[:2]
    (w2, h2) = face2.shape[:2]
    if(w1 > w2):
        face1 = crop_center(face1, (w2, h2))
    elif(w2 > w1):
        face2 = crop_center(face2, (w1, h1))
    return crop_circle(face1), crop_circle(face2)


def calc_similarity_between_faces(face1: Mat, face2: Mat) -> float:
    face1, face2 = equalize_faces(face1, face2)
    face1 = cv2.blur(face1, [5, 5])
    face2 = cv2.blur(face2, [5, 5])
    (w, h) = face1.shape[:2]
    errorL2 = cv2.norm(face1, face2, cv2.NORM_L2)
    return (1 - errorL2 / (h * w))
