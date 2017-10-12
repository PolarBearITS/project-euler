import itertools
import math
def is_prime(n):
	if n == 2:
		return True
	if n % 2 == 0 or n < 2:
		return False
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True

def esieve(n):
	b = {x:True for x in range(2, n+1)}
	for i in range(2, int(math.sqrt(n))+1):
		if b[i]:
			for j in range((n-i**2)//i + 1):
				b[i**2 + j*i] = False
	return [p for p in b if b[p]]

m = 0
limit = 1000000
primes = esieve(limit)
for i in range(len(primes)):
	for j in range(1, len(primes)-i+1):
		p = primes[i:i+j]
		l = len(p)
		s = sum(p)
		if s < limit:
			if m < l:
				if is_prime(s):
					m = l
					print(s, l)
		else:
			break