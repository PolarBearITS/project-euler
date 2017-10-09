import math

def is_pent(n):
	s = (math.sqrt(24*n + 1) + 1) / 6
	return s == int(s)

n = 1
is_p = False
while not is_p:
	n += 1
	p = n*(3*n - 1)//2
	for j in range(n-1, 0, -1):
		m = j*(3*j - 1)//2
		if is_pent(p + m) and is_pent(p - m):
			print(n, j, p - m)
			is_p = True
			break