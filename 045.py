import math
def is_pent(n):
	s = (math.sqrt(24*n + 1) + 1) / 6
	return s == int(s)

def is_hex(n):
	s = (math.sqrt(8*n + 1) + 1) / 4
	return s == int(s)


is_both = False
n = 285
t = 0
while not is_both:
	n += 1
	t = n*(n+1)//2
	is_both = is_pent(t) and is_hex(t)
print(t, n)