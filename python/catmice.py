# Cat and Mice game


def cat_mouse(player_number=100):
	c = 0
	c1 = 0
	c2 = 0
	c3 = 0
	for x in range(player_number + 1):
		prime = True
		for p in range(2, x):
			if (x % p == 0):
				prime = False
		if (x == 1) or (x == 0):
			prime = False
			print(x)
		elif prime:
			c3 = (c3 + 1)
			print("Dog")
		elif (x % 5 == 0) and (x % 3 == 0):
			c = (c + 1)
			print("Cat and Mouse")
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
	print("The total number of Cats is {}!".format(c1))
	print("The total number of Mice is {}!".format(c2))
	print("The total number of Dogs is {}!".format(c3))

cat_mouse()

