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

primes = esieve(1000000)
for prime in primes:
	if prime > 100000:
		x = str(prime)
		for i in range(1, len(x)+1):
			for combo in itertools.combinations(range(0, len(x)), i):
				family = []
				for j in range(10):
					new_str = list(x)
					for n in combo:
						new_str[n] = str(j)
					new_x = int(''.join(new_str))
					if is_prime(new_x) and len(str(new_x)) == len(x):
						if new_x not in family:
							family.append(new_x)
				if len(family) == 8:
					print(family)
					quit()