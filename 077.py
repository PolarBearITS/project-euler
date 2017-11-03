def sieve(n):
	a = [True] * (n + 1)
	a[0] = a[1] = False
	for i, p in enumerate(a):
		if p:
			yield i
			for j in range(i**2, n+1, i):
				a[j] = False

def prime_sum(n):
	primes = list(sieve(n))
	sums = {k:v for k, v in zip(range(1, n+1), [0]*n)}
	for prime in primes:
		for value in sums:
			if value == prime:
				sums[value] += 1
			elif value > prime:
				sums[value] += sums[value-prime]
	return sums[n]

n = 2
while True:
	x = prime_sum(n)
	if x > 5000:
		break
	else:
		n += 1
print(x, n)