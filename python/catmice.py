# Cat and Mice game


def cat_mouse(player_number=100):
	c = 0
	c1 = 0
	c2 = 0
	for x in range(player_number + 1):
		if (x % 5 == 0) and (x % 3 == 0):
			c = (c + 1)
			print("Cat and Mouse") and (c + 1)
		elif x % 3 == 0:
			c1 = (c1 + 1)
			print("Cat")
		elif x % 5 ==0:
			c2 = (c2 + 1)
			print("Mouse")
		else:
			print("{}".format(x))
		x += 1
	print("The total number of Cat and Mouse is {}!".format(c))
	print("The total number of Cat's is {}!".format(c1))
	print("The total number of Mice is {}!".format(c2))

cat_mouse()

