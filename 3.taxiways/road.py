def one_moov(right, left, up):
	if up == None:
		pass
	else:
		return up
	if right == None:
		pass
	else:
		return right
	if left == None:
		pass
	else:
		return left



def get_nb_moov(right, left, up):
	nb_moov = 3
	if right == None:
		nb_moov -= 1
	if left == None:
		nb_moov -= 1
	if up == None:
		nb_moov -= 1

	return nb_moov


def get_data():
	with open("data/data.txt", "r") as f:
		for line in f:
			return list(line)


def remove_moov(line):
	del line[0]


def get_angle(my_moov, right, left, up):
	corresponding = {"R":right, "L":left, "U":up}
	print(my_moov)
	return corresponding[str(my_moov)]