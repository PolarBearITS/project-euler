memo = {}
def factorial(n):
	if n in memo:
		return memo[n]
	else:
		f = 0
		if n == 0:
			f = 1
		else:
			f = n * factorial(n-1)
		memo[n] = f
	return f 

count = 0
limit = 1000000
for n in range(limit):
	chain = [n]
	end = False
	while not end:
		fsum = sum(map(factorial, (map(int, str(chain[-1])))))
		if fsum in chain:
			if len(chain) == 60:
				count += 1
				print(n)
			end = True
		else:
			chain.append(fsum)
print(count)