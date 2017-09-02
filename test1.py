cv2=__import__('cv2')
import matplotlib.pyplot as plt
import numpy

# start video capture
cap = cv2.VideoCapture(0)

while True:
    # read it
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # show it
    cv2.imshow('frame', frame)

    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()