from email.mime import base
import cv2
import numpy as np

base_img = cv2.imread(
    '../assets/images/U.png', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((3, 3), dtype=np.uint8)

base_img[base_img < 170] = 0

eroded_img = cv2.erode(base_img, kernel, anchor=(2, 2), iterations=70)


cv2.imshow('original', base_img)
cv2.imshow('erode', eroded_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
