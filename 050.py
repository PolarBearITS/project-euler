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

l = 0
primes = [0] + [p for p in range(5000) if is_prime(p)]
sums = {p:sum(primes[:primes.index(p) + 1]) for p in primes}
for i in range(len(primes)):
	for j in range(len(primes)-1, i-1, -1):
		s = sums[primes[j]] - sums[primes[i-1]]
		if l < s < 1000000 and is_prime(s):
			print(s, j - i)
			l = s
print(l)