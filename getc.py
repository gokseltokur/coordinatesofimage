
import argparse
import cv2
import os


arr = []

def click(event, x, y, flags, param):
	global refPt
	global cropping
	global arr

	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True

	elif event == cv2.EVENT_LBUTTONUP:
		refPt.append((x, y))
		cropping = False

		# draw a rectangle
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		arr = refPt.copy()
		###############
		#print(refPt[0], refPt[1])
		#print(refPt[0][0])
		###############
		#category = param.split("/")
		#print(param+","+str(refPt[0][0])+","+str(refPt[0][1])+","+str(refPt[1][0])+","+str(refPt[1][1])+","+category[0])
		#print(param)

		cv2.imshow("image", image)

f = open("kitti_simple_label.txt", "w")

path = 'images'
files = os.listdir(path)

for file in files:
	image = cv2.imread(path+'/'+file)
	#print(path+'/'+file)
	xx = path+'/'+file

	clone = image.copy()
	cv2.namedWindow("image")
	cv2.setMouseCallback("image", click, arr)

	#print(a, b)
	#f.write()


	while True:
		cv2.imshow("image", image)
		key = cv2.waitKey(1) & 0xFF

		# if you want to try again, press 'r'.
		if key == ord("r"):
			image = clone.copy()

		# if key pressed 'c', break loop.
		elif key == ord("c"):
			break
			
	f.write(xx+","+str(arr[0][0])+","+str(arr[0][1])+","+str(arr[1][0])+","+str(arr[1][1])+","+path+"\n")
	#print(arr)

	cv2.destroyAllWindows()
f.close()