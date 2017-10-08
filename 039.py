import math
l = 0
for i in range(1, 1001):
	solutions = []
	for a in range(1, i//2):
		for b in range(a, i//2):
			c = math.sqrt(a ** 2 + b ** 2)
			if int(c) == c and a + b + int(c) == i:
				solutions.append([a, b, int(c)])
	if len(solutions) > l:
		l = len(solutions)
		print(i, solutions, len(solutions))