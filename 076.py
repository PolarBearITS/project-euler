def ways(n):
	sums = {k:v for k, v in zip(range(n+1), [0]*(n+1))}
	sums[0] = 1
	for i in range(1, n):
		for value in sums:
			if value == i:
				sums[value] += 1
			elif value > i:
				sums[value] += sums[value-i]
	return sums[n]
x = ways(100)
print(x)