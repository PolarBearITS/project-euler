import itertools
import math
from decimal import Decimal
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

limit = 10**7
min_r = Decimal(limit)
max_n = 0
primes = list(sieve(5000))
for p in primes:
	for q in primes:
		n = p*q
		phi = (p-1)*(q-1)
		if n > limit:
			break
		if sorted(str(n)) == sorted(str(phi)) and n/phi < min_r:
			min_r = n/phi
			max_n = n
			print(p, q, n)