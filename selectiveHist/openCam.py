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

	mean = np.array([0, 0, 0])
	std = np.array([0, 0, 0])

	ret, frame = cap.read()

	cv2.namedWindow('Feed')
	cv2.setMouseCallback('Feed', drawBox)


	while(1):
		
		# Reads the next frame from the camera
		ret, frame = cap.read()

		if ret == False:
			break

		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		

		if cb.drawing == True:
			cv2.rectangle(frame, (cb.ix, cb.iy), (cb.fx, cb.fy), (255, 204, 51), 1)
			cutImg = hsv[cb.ix:cb.fx, cb.iy:cb.fx]
			displayHistograms(cutImg, hGraph, sGraph, vGraph)
			mean, std = cv2.meanStdDev(cutImg)
			print "The mean is: \n", mean
			print "The StdDev is: \n", std

		
		lowerRange = np.array([mean[0]-std[0], mean[1]-std[1], mean[2]-std[2]])
		upperRange = np.array([mean[0]+std[0], mean[1]+std[1], mean[2]+std[2]])

		mask = cv2.inRange(hsv, lowerRange, upperRange)

		res = cv2.bitwise_and(frame, frame, mask = mask)


		cv2.imshow('Feed', frame)
		cv2.imshow('Mask', mask)
		cv2.imshow('Filtered', res)

	    # Use 'Q' to exit program
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cv2.destroyAllWindows()
	cap.release()


def displayHistograms(img, hGraph, sGraph, vGraph):
			hist = cv2.calcHist([img], [0], None, [256], [0,256])
			hGraph.renderGraph(hist, (255, 0, 0))
			hist = cv2.calcHist([img], [1], None, [256], [0,256])
			sGraph.renderGraph(hist, (0, 255, 0))
			hist = cv2.calcHist([img], [2], None, [256], [0,256])
			vGraph.renderGraph(hist, (0, 0, 255))


dynamicColorMask()