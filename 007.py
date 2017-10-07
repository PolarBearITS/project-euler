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

n = 0
x = 1
while n != 10001:
	x += 1
	if is_prime(x):
		n += 1
print(x)