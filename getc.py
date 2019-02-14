
import argparse
import cv2
import os


def click(event, x, y, flags, param):
	global refPt, cropping

	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True

	elif event == cv2.EVENT_LBUTTONUP:
		refPt.append((x, y))
		cropping = False

		# draw a rectangle
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)


		###############
		print(refPt[0], refPt[1])
		###############


		cv2.imshow("image", image)


path = 'images'
files = os.listdir(path)

for file in files:
	image = cv2.imread(path+'/'+file)
	print(path+'/'+file)

clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click)


while True:
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF

	# if you want to try again, press 'r'.
	if key == ord("r"):
		image = clone.copy()

	# if key pressed 'c', break loop.
	elif key == ord("c"):
		break

cv2.destroyAllWindows()