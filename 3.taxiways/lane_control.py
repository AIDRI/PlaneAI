import cv2
import numpy as np
from PIL import Image
from lane_finding import angle_to_side, crop, select_rgb_yellow, convert_gray
from lane_finding import apply_smoothing, detect_edges, hough_lines, draw_lines
from road import one_moov, get_nb_moov, remove_moov, get_angle
from road import get_data


line = get_data()
moov_prec = 0
right = 0; right_it = 0; left = 0; left_it = 0; up = 0; up_it = 0; list_angle = []


while True:
	#replace line 17 by a line to capture display in real time, or by camera to capture in real life
	img = cv2.imread("data/two_lines.png")
	img = crop(img)
	yellow_img = select_rgb_yellow(img)
	gray_img = convert_gray(yellow_img)
	bluerred_img = apply_smoothing(gray_img)
	edge_img = detect_edges(bluerred_img)
	list_lines = hough_lines(edge_img)

	line_img, list_angle, right, left, up = draw_lines(img, list_lines, list_angle, right, right_it, left, left_it, up, up_it)
	#get right, left, up

	nb_moov = get_nb_moov(right, left, up)
	if nb_moov == 1:
		angle = one_moov(right, left, up)
	elif nb_moov != moov_prec:
		print(line[0])
		my_moov = line[0]
		angle = get_angle(my_moov, right, left, up)
		remove_moov(line)
	else:
		angle = get_angle(my_moov, right, left, up)
	moov_prec = nb_moov


	print("right :", right, "°") #right angle
	print("left :", left, "°") #left angle
	print("up :", up, "°") #up angle
	print("my angle :", angle) #final angle
	print("my moov :", my_moov) #moov to do
	print()
	print("*-*-*-*-*-*-*-*-*-*-*-*-*")
	print()

	cv2.imshow("line", line_img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break

cv2.destroyAllWindows()