import math
import itertools
def is_prime(n):
	if n <= 1:
		return False
	if n % 2 == 0 and n != 2:
		return False
	else:
		for i in range(3, int(math.sqrt(n)) + 1, 2):
			if n % i == 0:
				return False
	return True

def consecutive_quadratic_primes(a, b):
	n = 0
	primes = []
	last = False
	while not last:
		p = n**2 + a*n + b
		if is_prime(p):
			primes.append(p)
			n += 1
		else:
			last = True
	return primes

max_len = 0
for (a, b) in itertools.product(range(-999, 1000), range(-1000, 1001)):
	p = consecutive_quadratic_primes(a, b)
	if len(p) > max_len:
		max_len = len(p)
		print((a, b), a*b, p, len(p))