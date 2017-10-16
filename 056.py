m = 0
for a in range(100):
	for b in range(100):
		s = sum(map(int, str(a ** b)))
		if s > m:
			m = s
			print(a, b, s)
print(m)