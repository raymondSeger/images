cv2=__import__('cv2')
import matplotlib.pyplot as plt
import numpy

# start video capture
cap = cv2.VideoCapture(0)

while True:
    # read it
    ret, frame = cap.read()
    # show it
    cv2.imshow('frame', frame)

cap.release()
cv2.destroyAllWindows()