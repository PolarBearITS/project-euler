from math import sqrt
from collections import defaultdict
m = 100
squares = set([x**2 for x in range(int(m**(1/2) + 1))])
dio = list(set(range(m+1)) - squares)
max_x = 0
for d in dio:
	#Find the Fractional Period of d
	periods = defaultdict(list)
	a0 = int(sqrt(d))
	p = [a0]
	top = 1
	bottom = -a0
	while True:
		top1 = -bottom
		bottom1 = (d - top1 ** 2)//top
		period = 0
		while top1 > 0 or abs(top1) <= a0-bottom1:
			top1 -= bottom1
			period += 1
		if period not in periods or (period in periods and [top1, bottom1] not in periods[period]):
			periods[period].append([top1, bottom1])
			p.append(period)
		else:
			break
		top = bottom1
		bottom = top1
	convergents = []

	#Find convergents of d and check if they solve x^2 - dy^2 = 1
	a = 0
	b = 1
	x = p[0]*b + a
	y = b
	for i in range(10):
		if x**2 - d*y**2 == 1:
			# print(d, f': {x}^2 - {d} * {y}^2 = 1', [x, y])
			# print(x)
			if x > max_x:
				max_x = x
				print(d, x)
			break
		temp = a
		a = b
		b = b*p[1:][i % (len(p)-1)] + temp
		x = p[0]*b + a
		y = b
		convergents.append([x, y])