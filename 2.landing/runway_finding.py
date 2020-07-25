import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/runway_1.jpg', 0)


def dilation(img):
	kernel = np.ones((5,5), np.uint8) 
	return cv2.dilate(img,kernel,iterations = 1)


def threshold(img):
	_,th2 = cv2.threshold(img,10,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	return th2


def convolution_op(img, image):
	return cv2.bitwise_and(img, cv2.bitwise_not(image))


def detect_edges(image, low_threshold=40, high_threshold=150):
    return cv2.Canny(image, low_threshold, high_threshold)


def hough_lines(image):
    return cv2.HoughLinesP(image, rho=1, theta=np.pi/180, threshold=100, minLineLength=50, maxLineGap=200)


def delete_h(lines, new_lines):
	for line in lines:
	    print(line)
	    for x1,y1,x2,y2 in line:
	    	if (y2 - y1 > 200 or y1 - y2 > 200) and x2 - x1 < 300 and x2 - x1 > -300:
	    		new_lines.append(line)
	    		print(line)
	return new_lines


def draw_lines(image, lines, color=[0, 0, 255], thickness=3):
	for line in lines:
		for x1,y1,x2,y2 in line:
			cv2.line(image, (x1, y1), (x2, y2), color, thickness)
	return image


new_lines = []
image = dilation(img)
image = threshold(image)
image = detect_edges(image)
#image = convolution_op(imag, image)
lines = hough_lines(image)
lines = delete_h(lines, new_lines)
image = draw_lines(img, lines)

cv2.imshow("feed", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
