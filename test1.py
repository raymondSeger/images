cv2=__import__('cv2')
import matplotlib.pyplot as plt
import numpy

img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)

# show the picture
#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destryoAllWindows()

# show line
#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.plot([50,100], [80,100], 'c', linewidth=5)
#plt.show()

#save the image
cv2.imwrite('watchgray.png', img)