import cv2
import numpy as np

img = cv2.imread('../assets/images/source_01.png')

cv2.imshow('original', img)

(height, width) = img.shape[0:2]

low_width = int(width/3)
low_height = int(height/3)
low_quality_img = np.zeros((low_height, low_width, 3), np.uint8)


def nine2one(matrix):
    return matrix[1, 1]


for y in range(low_width):
    start_y = y * 3
    for x in range(low_height):
        start_x = x * 3
        target_3x3 = img[start_x:start_x+3, start_y: start_y+3]
        low_quality_img[x, y] = nine2one(target_3x3)


cv2.imshow('low quality', low_quality_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
