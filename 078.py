def pent(n):
	return [(1-n)*(2-3*n)//2, n*(3*n - 1)//2]

memo = {}
def ways(n):
	if n in globals()['memo']:
		return memo[n]
	if n == 0:
		return 1
	if n < 0:
		return 0
	signs = [1, 1, -1, -1]
	pents = [0]
	i = 1
	while n >= pents[-1]:
		pents += pent(i)
		i += 1
	s = 0
	for i, p in enumerate(pents[2:]):
		s += signs[i % 4]*ways(n-p)
	memo[n] = s
	return s
n = 0
while True:
	x = ways(n)
	if x % 1000000 == 0:
		break
	else:
		n += 1
print(x, n)