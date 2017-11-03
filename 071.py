import itertools
lim = 1000000

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

mn = 0
md = 1

for d in range(1, lim):
	n = int((3*d/7))
	if gcd(n, d) == 1 and 3/7 > n/d > mn/md:
		mn = n
		md = d
		print(n, d)