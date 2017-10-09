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

r = 10000
c = False
primes = [p for p in range(r) if is_prime(p)]
for i in range(3, r, 2):
	if i not in primes:
		if not any(s == int(s) for s in [math.sqrt((i - p) / 2) for p in primes if p < i]):
			print(i)