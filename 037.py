import math
def is_prime(n):
	if n == 2:
		return True
	if n % 2 == 0 or n < 2:
		return False
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True

p = []
i = 11
i = 10
while len(p) != 11:
	length = len(str(i))
	trunks = [int(str(i)[:l]) for l in range(length, 0, -1)] + [i % (10 ** l) for l in range(1, int(math.log(i, 10)) + 2)]
	if all(is_prime(t) for t in trunks):
		print(i)
		p.append(i)
	i += 1
print(p, sum(p))