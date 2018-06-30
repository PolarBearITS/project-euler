b = []
e = []
for line in open('099.txt').read().splitlines():
	l = list(map(int, line.split(',')))
	b.append(l[0])
	e.append(l[1])
m = 0
e0 = max(e)
for i in range(1000):
	n = b[i] ** (e[i]/e0)
	if n > m:
		m = n
		print(i + 1, b[i], e[i]) 