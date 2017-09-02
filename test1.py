import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

px = img[55,55] # [30 30 42] BGR = Blue Green Red)

# ROI = Region of Image
img[100:150, 100:150] = [255, 255, 255]

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

