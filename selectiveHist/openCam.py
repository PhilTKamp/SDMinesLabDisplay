import cv2
import numpy as np
from customHist import Graph
from cb import drawBox
import cb

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
	cv2.setMouseCallback('Feed', drawBox)


	while(1):
		
		# Reads the next frame from the camera
		ret, frame = cap.read()

		if ret == False:
			break

		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		
		cv2.rectangle(frame, (cb.ix, cb.iy), (cb.fx, cb.fy), (255, 204, 51), 1)

		if cb.drawing == True:
			cutImg = hsv[cb.ix:cb.fx, cb.iy:cb.fx]
			hist = cv2.calcHist([cutImg], [0], None, [256], [0,256])
			hGraph.renderGraph(hist, (255, 0, 0))
			hist = cv2.calcHist([cutImg], [1], None, [256], [0,256])
			sGraph.renderGraph(hist, (0, 255, 0))
			hist = cv2.calcHist([cutImg], [2], None, [256], [0,256])
			vGraph.renderGraph(hist, (0, 0, 255))



		cv2.imshow('Feed', frame)

	    # Use 'Q' to exit program
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cv2.destroyAllWindows()
	cap.release()

dynamicColorMask()