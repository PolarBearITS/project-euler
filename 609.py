import math
import mpmath
import itertools

def sieve(n):
	a = [True] * (n + 1)
	a[0] = a[1] = False
	for i, p in enumerate(a):
		if p:
			yield i
			for j in range(i**2, n+1, i):
				a[j] = False

def pi(n):
	if n < 2657:
		app = int(n/math.log(n))
		for i, x in enumerate(list(sieve(2658))[app:]):
			if x > n:
				return i + app
	else:
		app = int(mpmath.li(n))
		limit = math.ceil(math.sqrt(n)*math.log(n)/(8*math.pi))
		print(app, limit, list(itertools.islice(sieve(10**6), app-limit, app+limit)))

m0 = 2657
print(pi(m0))

# print(pi(10000000))
# while m[-1] != 1:
# 	x = pi(m[-1])
# 	m.append(x)
# 	print(m)