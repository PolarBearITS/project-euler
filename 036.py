def is_pal(n):
	return str(n) == str(n)[::-1]

s = 0
for i in range(1, 1000000):
	if is_pal(i) and is_pal(bin(i)[2:]):
		s += i
print(s)