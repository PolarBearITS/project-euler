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

for i in range(1000, 10000):
	perms = sorted(list(set([int(''.join(p)) for p in itertools.permutations(str(i)) if int(''.join(p)) > i])))
	if len(perms) >= 3:
		diffs = [p - i for p in perms]
		for d in diffs:
			if 2*d in diffs:
				candidates = [i, i + d, i + 2*d]
				if all(is_prime(c) for c in candidates):
					print(candidates, ''.join(map(str, candidates)))