import cv2
import numpy as np

base_img = cv2.imread('../assets/images/noise.jpg')

ksize = 7

median = cv2.medianBlur(base_img, ksize)


cv2.imshow('original', base_img)
cv2.imshow('median blur', median)

cv2.waitKey(0)
cv2.destroyAllWindows()
