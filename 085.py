w = 0
while True:
	w += 1
	for h in range(1, w+1):
		count = 0
		for i in range(1, w+1):
			for j in range(1, h+1):
				count += (h+1-j)*(w+1-i)
		if abs(count - 2000000) < 100:
			print(count, w, h, w*h)
			quit()