import cv2
import numpy as np
from customHist import Graph

def dynamicColorMask():
	# Begins reading from the default webcam
	cap = cv2.VideoCapture(0)

	hGraph = Graph("Hue")
	sGraph = Graph("Saturation")
	vGraph = Graph("Value")
	hGraph.openGraph()
	sGraph.openGraph()
	vGraph.openGraph()

	ret, frame = cap.read()

	cv2.namedWindow('Feed')

	while(1):
		
		# Reads the next frame from the camera
		ret, frame = cap.read()

		if ret == False:
			break

		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		hist = cv2.calcHist([hsv], [0], None, [256], [0,256])
		hGraph.renderGraph(hist, (255, 0, 0))
		hist = cv2.calcHist([hsv], [1], None, [256], [0,256])
		sGraph.renderGraph(hist, (0, 255, 0))
		hist = cv2.calcHist([hsv], [2], None, [256], [0,256])
		vGraph.renderGraph(hist, (0, 0, 255))
		

		cv2.imshow('Feed', hsv)

	    # Use 'Q' to exit program
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cv2.destroyAllWindows()
	cap.release()

dynamicColorMask()