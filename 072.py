limit = 1000000
count = 0
import math

def sieve(n):
	a = [True] * (n + 1)
	a[0] = a[1] = False
	for i, p in enumerate(a):
		if p:
			yield i
			for j in range(i**2, n+1, i):
				a[j] = False

def totient(n):
	t = n
	for p in globals()['primes']:
		if p > int(math.sqrt(n)) + 1:
			break
		if n % p == 0:
			while n % p == 0:
				n /= p
			t *= (1-1/p)
	if n > 1:
		t *= (1-1/n)
	return round(t)

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

primes = list(sieve(limit))
print(sum(totient(n) for n in range(2, limit + 1)))