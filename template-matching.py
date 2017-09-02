import cv2
import numpy as np

"""
Thus far, we load in both images, convert to gray. We keep the original RGB image, and create a grayscale version. I've mentioned this before, but the reason why we do this is because we do all of the processing in the grayscale version, then use the same coordinates for labels and such on the color image.
"""
img_rgb = cv2.imread('opencv-template-matching-python-tutorial.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('opencv-template-for-matching.jpg',0)
w, h = template.shape[::-1]

"""
With the main image, we just have the color version and the grayscale version. We load the template and note the dimensions.

Here, we call res the matchTemplate between the img_gray (our main image), the template, and then the matching method we're going to use. 
We specify a threshold, here 0.8 for 80%. Then we find locations with a logical statement, where the res is greater than or equal to 80%.

"""
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)

"""
Finally, we mark all matches on the original image, using the coordinates we found in the gray image:
"""
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Detected',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()