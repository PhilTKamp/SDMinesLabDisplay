# A file which contains a basic click and drag bounding box as a callback
# function for a window.

import cv2
import numpy as np

drawing = False
ix, iy = -1, -1
fx, fy = -1, -1

# Image callback function
def drawBox(event, x, y, flags, param):
	global ix, iy, fx, fy, drawing
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix, iy = x, y
		fx, fy = x, y

	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			fx, fy = x, y

	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False