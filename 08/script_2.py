from email.mime import base
import cv2
import numpy as np

base_img = cv2.imread('cars.png')

kernel_5 = np.ones((5, 5), np.uint8)
kernel_7 = np.ones((7, 7), np.uint8)

img_hsv = cv2.cvtColor(base_img, cv2.COLOR_BGR2HSV)

mask1 = cv2.inRange(img_hsv, (0, 50, 20), (5, 255, 255))
mask2 = cv2.inRange(img_hsv, (175, 50, 20), (180, 255, 255))
mask = cv2.bitwise_or(mask1, mask2)

# mask processing
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_5, iterations=2)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_7, iterations=10)
mask = cv2.dilate(mask, kernel_5, iterations=2)

blur_img = cv2.blur(base_img, (20, 20))
blur_img[mask > 0] = base_img[mask > 0]

cv2.imshow('original', base_img)
cv2.imshow('mask', mask)
cv2.imshow('blur', blur_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
