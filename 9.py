for x in range(1, 1000):
	for y in range(x+1, 1000-x):
		z = 1000-x-y
		print(x, y, z)
		if x ** 2 + y ** 2 == z ** 2:
			print(x * y * z)
			quit()