import numpy as np
import cv2
import serial
import time
try:
	cap = cv2.VideoCapture(2)
	ser = serial.Serial("COM6", 38400)
	ser.write(b'y')
    time.sleep(0.5)
	print(cap.set(3,1280))
	print(cap.set(4,720))
	while(True):
		# Capture frame-by-frame
		ret, frame = cap.read()

        blue,g,r = cv2.split(frame)
		# Our operations on the frame come here
		#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		r = r[117:609, 453:817]
        r = cv2.GaussianBlur(r, (31, 31), 0)
        (minVal, maxVal, cLoc, maxLoc) = cv2.minMaxLoc(r)
        cX, cY = cLoc
        cv2.circle(r, cLoc, 30, (0, 0, 0), 2)

        g = g[117:609, 453:817]
        g = cv2.GaussianBlur(g, (31, 31), 0)
        (minVal, maxVal, bLoc, maxLoc) = cv2.minMaxLoc(g)

        cv2.circle(g, bLoc, 30, (0, 255, 0), 2)
        bX, bY = bLoc

    if (cX - bX < -10 and cY - bY < -10):
        b = b'3'
    elif (cX - bX < -10 and cY - bY > 10):
        b = b'1'
    elif (cX - bX > 10 and cY - bY <-10):
        b = b'4'
    elif (cX - bX > 10 and cY - bY > 10):
        b = b'2'
    elif cX - bX < -10:
        b = b'r'
    elif cX - bX > 10:
        b = b'l'
    elif cY - bY < -10:
        b = b'd'
    elif cY - bY > 10:
        b = b'u'
    else:
        b = b'n'
    print(str(b))
    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imshow('frame2',r)
    cv2.imshow('frame3',g)
    sev.write(b)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
finally:		
	print("closing up shop")
	ser.close()
	cap.release()
	cv2.destroyAllWindows()
