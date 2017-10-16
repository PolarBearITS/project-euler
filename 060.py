import math
import itertools
import pickle
def is_prime(n):
	if n == 2:
		return True
	if n % 2 == 0:
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

def perm_primes(i, p1):
	perms = set()
	for p2 in primes[i+1:]:
		if is_prime(int(str(p1) + str(p2))) and is_prime(int(str(p2) + str(p1))):
			perms.add(p2)
	return perms

perm_sets = {}

result = 2 ** 32
primes = esieve(30000)
# for a, p in enumerate(primes):
# 	perm_sets[p] = perm_primes(a, p)
# 	print(p)
# with open('060.pk', 'wb') as f:
# 	pickle.dump(perm_sets, f)
with open('060.pk', 'rb') as f:
	perm_sets = pickle.load(f)
for a, p1 in enumerate(primes):
	for b, p2 in enumerate(primes[a+1:]):
		if p2 in perm_sets[p1]:
			for c, p3 in enumerate(primes[b+1:]):
				if p3 in perm_sets[p1] and p3 in perm_sets[p2]:
					for d, p4 in enumerate(primes[c+1:]):
						if p4 in perm_sets[p1] and p4 in perm_sets[p2] and p4 in perm_sets[p3]:
							for e, p5 in enumerate(primes[d+1:]):
								if p5 in perm_sets[p1] and p5 in perm_sets[p2] and p5 in perm_sets[p3] and p5 in perm_sets[p4]:
									if result > p1 + p2 + p3 + p4 + p5:
										result = p1 + p2 + p3 + p4 + p5
										print(p1, p2, p3, p4, p5)
										print(result)