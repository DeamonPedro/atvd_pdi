import cv2
import numpy as np

base_img = cv2.imread(
    '../assets/images/U.png', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((9, 5), dtype=np.uint8)

base_img[base_img < 170] = 0

eroded_img = cv2.erode(base_img, kernel, iterations=50)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (150, 150))

dilated_img = cv2.dilate(eroded_img, kernel)

cv2.imshow('original', base_img)
cv2.imshow('res', dilated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
