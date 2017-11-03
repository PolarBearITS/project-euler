from math import sqrt
from collections import defaultdict
limit = 10000
squares = [x**2 for x in range(int(sqrt(limit)) + 1)]
odds = 0
for n in range(limit + 1):
	a0 = int(sqrt(n))
	if a0 ** 2 == n:
		continue
	periods = defaultdict(list)
	top = 1
	bottom = -a0
	while True:
		top1 = -bottom
		bottom1 = (n - top1 ** 2)//top
		period = 0
		while top1 > 0 or abs(top1) <= a0-bottom1:
			top1 -= bottom1
			period += 1
		if period not in periods or (period in periods and [top1, bottom1] not in periods[period]):
			periods[period].append([top1, bottom1])
		else:
			break
		top = bottom1
		bottom = top1
	period_len = len([v for value in periods.values() for v in value])
	print(n, period_len)
	if period_len % 2 == 1:
		odds += 1
print(odds)