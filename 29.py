import itertools
def distinct_powers(n):
	powers = []
	l = itertools.product(range(2, n + 1), range(2, n + 1))
	for a, b in l:
		x = a**b
		if x not in powers:
			powers.append(x)
	return sorted(powers)

p = distinct_powers(100)
print(len(p))