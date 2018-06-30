from math import sqrt
m = 0
a = 1
done = False
while not done:
	a += 1
	for c in [a-1, a+1]:
		s = a + c/2
		if 2*a + c > 10000000:
			done = True
		a = ((s-a)**2)*(s*(s-c))
		if round(sqrt(a))
		if area == int(area) and area > 0:
			print(a, a, c, int(area), 2*s)
			m += 2*a + c
print(m)