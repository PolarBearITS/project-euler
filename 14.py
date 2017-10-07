def collatz(n):
	s = [n]
	while s[-1] != 1:
		x = s[-1]
		if x % 2 == 0:
			x //= 2
			s.append(x)
		else:
			x = 3*x + 1
			s.append(x)
	return s

maximum = 0
n = 0
for i in range(1, 1000000):
	c = collatz(i)
	l = len(c)
	if l > maximum:
		print(i)
		maximum = l
		n = i

print(n, maximum, collatz(n))