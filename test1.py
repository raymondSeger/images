import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

px = img[55,55] # [30 30 42] BGR = Blue Green Red)

# ROI = Region of Image
img[100:150, 100:150] = [255, 255, 255]

# copy some region BGR values and then paste that to another region BGR, effectively copy pasting it like photoshop
watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

