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

def rotr(n):
	n = str(n)
	if len(n) == 1:
		return n
	return n[-1:] + n[:-1]

def rotate_prime(n):
	p = [str(n)]
	i = rotr(n)
	while int(i) != n:
		if not is_prime(int(i)):
			return False
		p.append(i)
		i = rotr(i)
	return True

rp = []
for i in range(2, 1000000):
	if is_prime(i):
		if rotate_prime(i):
			rp.append(i)
print(rp, sum(rp), len(rp))