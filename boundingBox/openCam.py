from cb import drawBox
import cb
import cv2
import numpy as np

def dynamicColorMask():
	# Begins reading from the default webcam
	cap = cv2.VideoCapture(0)

	ret, frame = cap.read()

	cv2.namedWindow('Feed')
	cv2.setMouseCallback('Feed', drawBox)

	while(1):
		
		# Reads the next frame from the camera
		ret, frame = cap.read()

		if ret == False:
			break

		cv2.rectangle(frame, (cb.ix, cb.iy), (cb.fx, cb.fy), (255, 204, 51), 1)

		cv2.imshow('Feed', frame)

	    # Use 'Q' to exit program
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cv2.destroyAllWindows()
	cap.release()

dynamicColorMask()