import cv2
import numpy as np

img = cv2.imread('coins.jpeg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img_gray, 100, 200)
cv2.imshow('edges', edges)
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT,
                           1, 100, param1=200, param2=50, minRadius=50, maxRadius=150)
circles = np.uint16(np.around(circles))
print(len(circles[0, :]))
for i in circles[0, :]:
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(img, (i[0], i[1]), 2, (255, 0, 0), 3)
cv2.imshow('HoughCircles', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
