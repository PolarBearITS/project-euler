from collections import defaultdict
def sieve(n):
	a = [True] * (n + 1)
	a[0] = a[1] = False
	for i, p in enumerate(a):
		if p:
			yield i
			for j in range(i**2, n+1, i):
				a[j] = False
n = 100
factors = defaultdict(int)
for i in range(2, n + 1):
	d = defaultdict(int)
	for p in sieve(n):
		while i % p == 0:
			i //= p
			d[p] += 1
	for k, v in d.items():
		if factors[k] < v:
			factors[k] = v
m = 1
for k, v in factors.items():
	m *= (k ** v)
print(m)