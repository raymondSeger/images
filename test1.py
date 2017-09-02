import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

px = img[55,55] # [30 30 42] BGR = Blue Green Red)

print(px)

# ROI = Region of Image
roi = img[100:150, 100:150]
print(roi)