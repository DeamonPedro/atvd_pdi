import cv2
import numpy as np

base_img = cv2.imread('ifma-caxias.jpg')
target_img = cv2.imread('logo-if.jpg')
target_img = cv2.resize(target_img, (200, 100), interpolation=cv2.INTER_AREA)
target_area = base_img[0:100, 0:200]

target_gray = cv2.cvtColor(target_img, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(target_gray, 125, 255, cv2.THRESH_BINARY)
target_area[mask == 0] = (0, 0, 0)

adaptedMask = np.zeros(target_area.shape, np.uint8)

base_img[0:100, 0:200] = cv2.inpaint(target_area, cv2.cvtColor(adaptedMask, cv2.COLOR_BGR2GRAY), 3, cv2.INPAINT_NS)

cv2.imshow('result', base_img)

cv2.waitKey(0)
cv2.destroyAllWindows()