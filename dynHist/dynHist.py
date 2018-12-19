import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import cv2
import numpy as np


def animate(i):
	global cap, fig
	ret, frame = cap.read()

	#Error properly displaying image to window
	#cv2.imshow('Feed', frame)

	color = ('b', 'g', 'r')

	fig.clear()
	for i,col in enumerate(color):
		hist = cv2.calcHist([frame], [i], None, [256],[0,256])
		plt.plot(hist,color = col)
		plt.xlim([0,256])

fig = plt.figure()
cap = cv2.VideoCapture(0)
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
cap.release()
cv2.destroyAllWindows()