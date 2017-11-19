n = 50000000
import math
def sieve(n):
	a = [True] * (n + 1)
	a[0] = a[1] = False
	for i, p in enumerate(a):
		if p:
			yield i
			for j in range(i**2, n+1, i):
				a[j] = False

primes = list(sieve(int(math.sqrt(n))))
s = int(math.sqrt(n))
nums = [0]*n
for q in primes:
	if q**4 > n:
		break
	for t in primes:
		if q**4 + t**3 > n:
			break
		for d in primes:
			p = d**2 + t**3 + q**4
			if p > n:
				break
			nums[p] += 1
count = n - nums.count(0)
print(count)