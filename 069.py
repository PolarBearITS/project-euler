def sieve(n):
	a = [True] * (n + 1)
	a[0] = a[1] = False
	for i, p in enumerate(a):
		if p:
			yield i
			for j in range(i**2, n+1, i):
				a[j] = False

limit = 1000000

n = 1
for p in sieve(limit):
	m = n * p
	if m <= limit:
		n = m
print(n)