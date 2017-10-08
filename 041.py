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

l = 0
for d in range(1, 9):
	for combo in itertools.permutations(range(1, d), d-1):
		n = int(str(d) + ''.join(map(str, combo)))
		if is_prime(n) and n > l:
			l = n
			print(n)