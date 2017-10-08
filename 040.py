import math
c = ''
i = 1
d = 0
e = 0
m = 1
while len(c) < 1000000:
	for n in str(i):
		d += 1
		if d == 10**e:
			e += 1
			m *= int(n)
			print(n)
		c += n
	i += 1
print(d)
print(m)