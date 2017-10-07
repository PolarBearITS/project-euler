from collections import defaultdict
primes = [2, 3, 5, 7, 11, 13, 17, 19]
n = 20
factors = defaultdict(int)
for i in range(2, n + 1):
	d = defaultdict(int)
	for p in primes:
		while i % p == 0:
			i //= p
			d[p] += 1
	print(d)
	for k, v in d.items():
		if factors[k] < v:
			factors[k] = v
print()
print(factors)
m = 1
for k, v in factors.items():
	m *= (k ** v)
print(m)