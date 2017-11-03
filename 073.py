import itertools
lim = 12000

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

count = 0

for d in range(3, lim+1):
	if d % 1000 == 0:
		print(d)
	for n in range(int(d/3)+1, int(d/2)+1):
		if gcd(n, d) == 1:
			count += 1
print(count)