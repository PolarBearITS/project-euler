import math
import itertools
tests = {
	3:lambda x:1+8*x,
	4:lambda x:x,
	5:lambda x:1+24*x,
	6:lambda x:1+8*x,
	7:lambda x:9+40*x,
	8:lambda x:4+12*x,
}
length = 3
def get_poly(x):
	types = []
	for t, l in tests.items():
		s = math.sqrt(l(x))
		if s == int(s):
			types.append(t)
	return types

cycle = []
poly = []
firsts = {}
if len(cycle) == 0:
	for m in range(10, 100):
		for n in range(10, 100):
			i = int(str(m) + str(n))
			p = get_poly(i)
			if len(p) > 0:
				firsts[i] = p

for first in firsts:
	cycle.append(first)
	poly.append(firsts[first])
	print(cycle, poly)
	for m in range(length-1):
		end = str(cycle[m])[-2:]
		print(end)
		for n in range(10, 100):
			i = int(str(end) + str(n))
			p = get_poly(i)
			if len(p) > 0 and any(t not in itertools.chain.from_iterable(poly) for t in p):
				print(i, p)
		quit()
	quit()