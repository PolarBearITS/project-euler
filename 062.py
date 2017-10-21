import itertools
perms = []
n = 0
while len(perms) < 5:
	perms = []
	n += 1
	print(n)
	m = sorted(str(n**3), reverse=True)
	l = int(int(''.join(m)) ** (1/3))+1
	for i in range(n, l):
		if sorted(str(i**3), reverse=True) == m:
			perms.append(i**3)
print(perms, n)