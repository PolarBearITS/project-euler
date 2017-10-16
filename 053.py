import itertools
import math
e = []
for n in itertools.product(range(1, 101), range(1, 101)):
	if n[0] >= n[1]:
		c = math.factorial(n[0]) // (math.factorial(n[1]) * math.factorial(n[0]-n[1]))
		if c > 1000000:
			e.append(n)
print(len(e))