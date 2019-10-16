import cv2
try:
	cap = cv2.VideoCapture(2)
	print(cap.set(3, 1280))
	print(cap.set(4, 720))
	while True:
		# Capture frame-by-frame
		ret, frame = cap.read()
		s = frame.copy()
		s = cv2.cvtColor(s, cv2.COLOR_BGR2GRAY)
		ret, s = cv2.threshold(s, 200, 255, cv2.THRESH_BINARY)
		
		# Display the resulting frame
		cv2.imshow('frame', frame)
		cv2.imshow('score', s)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

# When everything done, release the capture
finally:		
	print("Cleaning up...")
	cap.release()
	cv2.destroyAllWindows()
