# SDMinesLabDisplay
This repo will, in the future, be a collection of some OpenCV Code and OpenCV Programs to be used as a display within the SD Mines UAS and Robotics Lab.<br /><br />

Currently, the repo only contains a single program focused on dynamic color masking for tours. To run this program, git clone the repo and run openCam.py within the dynamicMask directory.<br /><br />

There will then be 6 windows which appear they are as following:<br />
&nbsp;&nbsp;&nbsp;&nbsp;Feed: The unaltered feed from the default webcam<br />
&nbsp;&nbsp;&nbsp;&nbsp;Mask: The Mask which is being applied to the Feed<br />
&nbsp;&nbsp;&nbsp;&nbsp;Filtered: The result of masking the Feed<br />
&nbsp;&nbsp;&nbsp;&nbsp;Hue: A histogram of the different hue values within the ROI<br />
&nbsp;&nbsp;&nbsp;&nbsp;Saturation: A histogram of the different saturation values within the ROI<br />
&nbsp;&nbsp;&nbsp;&nbsp;Value: A histogram of the different color calues within the ROI<br />

To select a ROI simply hold left click and drag on the Feed window. The mask is generated based on the thresholds of all previous masks and the new HSV Thresholds found from the new ROI.<br /><br />

Current Known Bugs: <br />
&nbsp;&nbsp;&nbsp;&nbsp;The ROI will only properly register if the user drags from the top of their desired ROI to the bottom right.<br />
&nbsp;&nbsp;&nbsp;&nbsp;Certain Colors will not be found by the ROI, unknown whether this is a calculation issue from mean and stddev, or if it's due to selecting too small regions.<br />
&nbsp;&nbsp;&nbsp;&nbsp;Program kicks back a single divide by zero warning from the CustomHist source file.<br /><br />

To Do:<br />
&nbsp;&nbsp;&nbsp;&nbsp;Apply noise reduction to the HSV mask creation
