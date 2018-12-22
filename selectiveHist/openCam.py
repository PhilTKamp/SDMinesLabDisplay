import cv2
import numpy as np
from customHist import Graph
from cb import drawBox
import cb

def dynamicColorMask():
	# Begins reading from the default webcam
	cap = cv2.VideoCapture(0)

	# Initializes all histogram windows
	hGraph = Graph("Hue")
	sGraph = Graph("Saturation")
	vGraph = Graph("Value")
	hGraph.openGraph()
	sGraph.openGraph()
	vGraph.openGraph()

	# Sets starting values for HSV color bounds
	minVals = np.array([255, 255, 255])
	maxVals = np.array([0, 0, 0])

	# Opens the primary window for the user and sets the callback for drawing
	cv2.namedWindow('Feed')
	cv2.setMouseCallback('Feed', drawBox)


	while(1):
		
		# Reads the next frame from the camera
		ret, frame = cap.read()

		# Breaks if error reading video
		if ret == False:
			break

		# Gets an HSV version for color detection
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		
		# Sets the ranges for the HSV based color mask
		lowerRange = np.array([minVals[0], minVals[1], minVals[2]])
		upperRange = np.array([maxVals[0], maxVals[1], maxVals[2]])

		# If we're drawing a new rectangle calculate values and display rectangle
		if cb.drawing == True:
			cv2.rectangle(frame, (cb.ix, cb.iy), (cb.fx, cb.fy), (255, 204, 51), 1)

			# Extracts the image selected by ROI rectangle and recalculates the min/max vals
			cutImg = hsv[cb.ix:cb.fx, cb.iy:cb.fx]
			displayHistograms(cutImg, hGraph, sGraph, vGraph)
			mean, std = cv2.meanStdDev(cutImg)

			for i in range(0, 3, 1):
				minVals[i] = min(minVals[i], mean[i] - std[i])
				maxVals[i] = max(maxVals[i], mean[i] + std[i])


		# Generates mask based on range, applies mask
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

# Funtion written for readability, just updates the histograms
def displayHistograms(img, hGraph, sGraph, vGraph):
			hist = cv2.calcHist([img], [0], None, [256], [0,256])
			hGraph.renderGraph(hist, (255, 0, 0))
			hist = cv2.calcHist([img], [1], None, [256], [0,256])
			sGraph.renderGraph(hist, (0, 255, 0))
			hist = cv2.calcHist([img], [2], None, [256], [0,256])
			vGraph.renderGraph(hist, (0, 0, 255))


dynamicColorMask()