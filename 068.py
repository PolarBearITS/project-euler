import itertools
from collections import defaultdict
ngon = 5

def check(x, y):
	return x[-1] == y[1] and sum(x) == sum(y) and set(x) != set(y)

def check_middle(l):
	x = {(i*len(a) + j):b for i, a in enumerate(l) for j, b in enumerate(a)}
	m = {k:v for k, v in x.items() if k % 3 == 0}
	return all(list(x.values()).count(y) == 1 for y in m.values())

r = range(1, 2*ngon+1)

for a in itertools.permutations(r, 3):
	for b in itertools.permutations(r, 3):
		if a[0] < b[0] and check(a, b):
			for c in itertools.permutations(r, 3):
				if a[0] < c[0] and check(b, c):
					for d in itertools.permutations(r, 3):
						if a[0] < d[0] and check(c, d):
							# if d[-1] == a[1] and check_middle([a, b, c, d]):
							# 	print(a, b, c, d, sum(a))
							for e in itertools.permutations(r, 3):
								if a[0] < e[0] and check(d, e):
									l = [a, b, c, d, e]
									if e[-1] == a[1] and check_middle(l):
										x = [b for a in l for b in a]
										y = ''.join(map(str, x))
										if len(y) == 16:
											print(l, y)