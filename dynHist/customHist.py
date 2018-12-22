import cv2
import numpy as np 

class Graph:

	# Default size values were chosen as it'll be a histogram for color detection
	def __init__(self, name, winWidth = 587, winHeight = 275):
		self.winWidth = winWidth
		self.winHeight = winHeight
		self.name = name
		self.graph = np.zeros((winHeight, winWidth, 3))

	# Simply opens a blank window for the histogram
	def openGraph(self):
		cv2.namedWindow(self.name)
		cv2.imshow(self.name, self.graph)

	def renderGraph(self, data = [], color = (0, 0, 0)):
		# Clears "old data" from the image
		self.graph = np.full((self.winHeight, self.winWidth, 3), 255)

		self.drawAxis()

		# Normalizes all points on y-axis
		heightScalar = 200 / max(data)

		# The starting offset for the graph index
		xIndex = 50;
		points = np.array([])

		# Adds all of the points for the graph to an array
		for value in data:
			points = np.append(points, [xIndex, 50 + (value * heightScalar)])
			xIndex += 2

		# Reshapes the points array to match polylines requirements
		# (Not fully certain yet why this is necessary)
		points = points.reshape(-1, 1, 2)
		cv2.polylines(self.graph, np.int32([points]), False, color)

		# Flips the graph (We draw from top right to bottom left)
		self.graph = cv2.flip(self.graph, 0)

		# Displays the graph
		cv2.imshow(self.name, self.graph)


	def drawAxis(self):

		#Draws y-axis indicator
		cv2.line(self.graph, (50, 50), (50, 250), (0, 0, 0), 1)

		#Draws x-axis indicator
		cv2.line(self.graph, (50, 50), (562, 50), (0,0,0), 1)
