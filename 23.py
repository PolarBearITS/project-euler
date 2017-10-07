import functools
import itertools
def factors(n):
	f = list(set(functools.reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
	f.remove(n)
	return f

bound = 28123
abundants = []
for i in range(1, bound+1):
	if sum(factors(i)) > i:
		abundants.append(i)
abundant_sums = set()
for i in range(len(abundants)):
	for j in range(i, len(abundants)):
		if abundants[i] + abundants[j] <= bound:
			abundant_sums.add(abundants[i] + abundants[j])

non_abundant_sums = set(range(1, bound+1)) - abundant_sums
print(non_abundant_sums)
print(sum(non_abundant_sums))