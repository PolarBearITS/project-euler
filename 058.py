import math
def is_prime(n):
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True

ratio = 1
gap = 0
p = 1
n = 0
while ratio > 0.1:
	if math.sqrt(p) == int(math.sqrt(p)):
		if n != 0:
			ratio = n/(2*gap + 1)
			print(ratio, gap + 1)
		gap += 2
	p += gap
	if is_prime(p):
		n += 1