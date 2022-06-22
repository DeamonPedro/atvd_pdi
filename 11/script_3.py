from email.mime import base
import cv2
import numpy as np

base_img = cv2.imread('atividade_aula11.png',cv2.IMREAD_GRAYSCALE)
base_img[base_img < 170] = 0

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(150,150))

dilated_img = cv2.dilate(base_img, kernel)

cv2.imshow('original', base_img)
cv2.imshow('res', dilated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
