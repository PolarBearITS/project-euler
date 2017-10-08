l = 0
for i in range(10000):
	concat = ''
	m = 1
	while len(concat) < 9:
		concat += str(i*m)
		m += 1
	if len(concat) > 9:
		continue
	if all(str(d) in concat for d in range(1, 10)):
		if int(concat) > l:
			l = int(concat)
			print(concat, i, list(range(1, m)))