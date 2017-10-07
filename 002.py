memo = {}
def fib(n):
	if n in memo: return memo[n]
	if n <= 2: f = 1
	else: f = fib(n-1) + fib(n-2)
	memo[n] = f
	return f

s = 0
for i in range(50):
	x = fib(i)
	if x < 4000000:
		if x % 2 == 0:
			s += x
	else:
		break
print(s)