m = {}
def fib(n):
	if n in m:
		return m[n]
	elif n <= 2:
		return 1
	else:
		f = fib(n-1) + fib(n-2)
		m[n] = f
		return f

i = 1
while len(str(fib(i))) != 1000:
	i += 1
print(i)