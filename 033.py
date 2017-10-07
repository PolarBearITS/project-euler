import itertools

def replace(s, c):
	return s[:s.index(c)] + s[s.index(c) + 1:]

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

numerator = 1
denominator = 1
for n in range(10, 100):
	for d in range(n + 1, 100):
		com = [c for c in str(n) if c in str(d)]
		if len(com) > 0:
			com = com[0]
			if com != '0':
				n1 = int(replace(str(n), com))
				d1 = int(replace(str(d), com))
				if d1 != 0:
					if n / d == n1 / d1:
						numerator *= n
						denominator *= d
g = gcd(numerator, denominator)
print(numerator//g, denominator//g)