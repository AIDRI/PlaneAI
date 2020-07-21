import cv2
import numpy as np
from PIL import Image

def angle_to_side(x, right, right_it, left, left_it, up, up_it):
	if x > 100 or x < -100:
		left += np.abs(x)
		left_it += 1
		return "left", left, left_it, right, right_it, up, up_it
	elif -80 < x < 80:
		right += np.abs(x)
		right_it += 1
		return "right", left, left_it, right, right_it, up, up_it
	elif -80 >= x >= -100 or 80 <= x <= 100:
		up += np.abs(x)
		up_it += 1
		return "up", left, left_it, right, right_it, up, up_it
	raise KeyError

def crop(img):
	height, width, _ = img.shape
	y=531; x=300; h=818; w=width-300
	img = img[y:h, x:w]
	return img


def select_rgb_yellow(image): 
    lower = np.uint8([60, 93, 30])
    upper = np.uint8([75, 255, 255])
    yellow_mask = cv2.inRange(image, lower, upper)
    masked = cv2.bitwise_and(image, image, mask = yellow_mask)
    return masked


def convert_gray(image):
	return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


def apply_smoothing(image, kernel_size=15):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)


def detect_edges(image, low_threshold=50, high_threshold=150):
    return cv2.Canny(image, low_threshold, high_threshold)


def hough_lines(image):
    return cv2.HoughLinesP(image, rho=1, theta=np.pi/180, threshold=15, minLineLength=18, maxLineGap=500)


def draw_lines(image, lines, list_angle, right, right_it, left, left_it, up, up_it, color=[255, 0, 0], thickness=2):
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(image, (x1, y1), (x2, y2), color, thickness)
            answer, left, left_it, right, right_it, up, up_it = angle_to_side(np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi, right, right_it, left, left_it, up, up_it)
            list_angle.append(answer)

    try:right = round(90 - right/right_it, 3)
    except:right = None
    try:left = round(90 - left/left_it, 3)
    except:left = None
    try:up = round(90 - up/up_it, 3)
    except:up = None
    return image, list_angle, right, left, up


list_angle = []
img = cv2.imread("two_lines.png")
img = crop(img)
yellow_img = select_rgb_yellow(img)
gray_img = convert_gray(yellow_img)
bluerred_img = apply_smoothing(gray_img)
edge_img = detect_edges(bluerred_img)

line = hough_lines(edge_img)
right = 0; right_it = 0; left = 0; left_it = 0; up = 0; up_it = 0
line_img, list_angle, right, left, up = draw_lines(img, line, list_angle, right, right_it, left, left_it, up, up_it)


print(np.unique(list_angle))
print("right :", right, "°")
print("left :", left, "°")
print("up :", up, "°")

cv2.imshow("line", line_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
