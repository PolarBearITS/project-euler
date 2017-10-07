import functools
def factors(n):
	f = list(functools.reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
	f.remove(n)
	return f

amicable = []
for i in range(1, 10000):
	j = sum(factors(i))
	if j not in amicable:
		if sum(factors(j)) == i:
			if i != j:
				amicable += [i, j]
print(amicable, sum(amicable))