import math
from collections import defaultdict
limit = 1500000

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

triangles = defaultdict(int)
n = 0

for u in range(2, int(math.sqrt(limit/2)) + 1):
	for v in range(1, u):
		if (u + v) % 2 == 1 and gcd(u, v) == 1:
			a = u**2 - v**2
			b = 2*u*v
			c = u**2 + v**2
			l = a + b + c
			while l <= limit:
				triangles[l] += 1
				if triangles[l] == 1:
					n += 1
				elif triangles[l] == 2:
					n -= 1
				l += a + b + c

print(n)