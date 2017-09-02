cv2=__import__('cv2')
import matplotlib.pyplot as plt
import numpy

# start video capture
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID') #codec to use
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480)) #output and size and frame

while True:
    # read it
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame) #write data to the output file

    # show it
    cv2.imshow('frame', frame)

    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release() #release
cv2.destroyAllWindows()