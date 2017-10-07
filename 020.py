def factorial(n):
	if n == 1:
		return 1
	else:
		return n*factorial(n-1)

print(sum(map(int, str(factorial(100)))))