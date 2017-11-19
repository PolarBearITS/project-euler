n = 10000000
memo = {}
count = 0
for i in range(1, n):
	new = []
	c = i
	while c not in [1, 89]:
		if c in memo:
			c = memo[c]
			break
		else:
			new.append(c)
			c = sum(int(s)**2 for s in str(c))
	for n in new:
		memo[n] = c
	if c == 89:
		count += 1
print(count)