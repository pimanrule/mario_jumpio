import numpy as np
import cv2
import serial
import time

# Which video input is your capture card?
CAPTURE_CARD_INDEX = 2
CAPTURE_CARD_WIDTH = 1280
CAPTURE_CARD_HEIGHT = 720
# On which virtual serial port is your microcontroller connected to?
SERIAL_PORT = "COM6"
SERIAL_BAUD_RATE = 38400

frequency = 2500  
duration = 33
previousScoreDisplay = None

try:
    capture = cv2.VideoCapture(CAPTURE_CARD_INDEX)
    capture.set(3, CAPTURE_CARD_WIDTH)
    capture.set(4, CAPTURE_CARD_HEIGHT)
    ser = serial.Serial(COM_PORT, SERIAL_BAUD_RATE)
    while (cv2.waitKey(1) & 0xFF) != ord('q'):
        _, frame = capture.read()
        # Crop the captured frame to just have the score in the bottom-right
        scoreDisplay = frame[507:587, 1051:1235]
        scoreDisplay = cv2.cvtColor(scoreDisplay, cv2.COLOR_BGR2GRAY)
        _, scoreDisplay = cv2.threshold(scoreDisplay, 200, 255, cv2.THRESH_BINARY)
        
        if previousScoreDisplay != None:
            diff = (np.sum(np.abs(np.subtract(scoreDisplay, previousScoreDisplay))))/1000
            print(diff)
            if diff > 4.7:
                print("\a")
                time.sleep(23.2/60)
                ser.write(b'b')
        
        # Display the frame and filtered score display, each in a separate window
        cv2.imshow('frame', frame)
        cv2.imshow('score display (processed)', scoreDisplay)
        previousScoreDisplay = scoreDisplay.copy()

# When everything done, release the capture
finally:        
    print("closing up shop")
    ser.close()
    capture.release()
    cv2.destroyAllWindows()
