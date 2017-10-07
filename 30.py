d = []
for i in range(2, 1000000):
	s = sum([x ** 5 for x in map(int, str(i))])
	if i == s:
		print(i)
		d.append(i)
print(sum(d))