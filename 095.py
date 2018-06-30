import functools
def factors(n):
	f = list(functools.reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
	f.remove(n)
	return f

def next_amicable(n):
	return sum(factors(n))

def amicable_chain(n):
	chain = [n]
	o = n
	while True:
		o = next_amicable(o)
		if o in memo:
			chain += memo[o]
			break
		chain.append(o)
		if chain[-1] in chain[:-1] or o > 1000000:
			break
	if chain[0] == chain[-1]:
		memo[n] = chain[:-1]
		return memo[n]
	else:
		return []

global memo
memo = {}

m = 0
for n in range(1, 20000):
	c = amicable_chain(n)
	if c != []:
		if len(c) > m:
			m = len(c)
			chain = c
			print(n, min(c), c)
