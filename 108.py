def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def lcm(a, b):
	return a*b//gcd(a, b)

n = 4
count = 0
for i in range(n + 1, 2*n + 1):
	x, y = i, lcm(n, i)
	if y//x + 1 == y//n:
		count += 1