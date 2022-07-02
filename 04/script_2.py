import cv2
import numpy as np

img = cv2.imread('../assets/images/source_01.png')

cv2.imshow('original', img)

(height, width) = img.shape[0:2]
low_quality_img = np.zeros(img.shape, np.uint8)


def nine2one(matrix):
    return cv2.mean(matrix)[:3]


for y in range(width):
    for x in range(height):
        target_3x3 = img[x-1:x+2, y-1: y+2]
        low_quality_img[x, y] = nine2one(target_3x3)


cv2.imshow('low quality', low_quality_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
