import math
from collections import defaultdict
limit = 1000
max_x = 0
for d in range(2, limit+1):
	a0 = int(math.sqrt(d))
	if a0 ** 2 == d:
		continue
	periods = defaultdict(list)
	p = []
	n0 = 1
	d0 = -a0
	while True:
		n1 = -d0
		d1 = (d - n1 ** 2)//n0
		period = 0
		while n1 > 0 or abs(n1) <= a0 - d1: 
			n1 -= d1
			period += 1
		if period in periods and [n1, d1] in periods[period]:
			break
		else:
			periods[period].append([n1, d1])
			p.append(period)
		n0 = d1
		d0 = n1

	a = [1, a0]
	b = [0, 1]
	i = 0
	while True:
		x = p[i%len(p)]*a[-1] + a[-2]
		y = p[i%len(p)]*b[-1] + b[-2]
		a = a[-1:] + [x]
		b = b[-1:] + [y]
		if x ** 2 - d * y**2 == 1:
			if x > max_x:
				max_x = x
				print(d, i, x, y)
			break
		i += 1