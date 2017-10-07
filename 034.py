memo = {}
def factorial(n):
	if n in memo: return memo[n]
	if n <= 1: return 1
	else: f = n*factorial(n-1)
	memo[n] = f
	return f

nums = []
product = 1
for i in range(1, 100000):
	if i == sum(map(factorial, map(int, str(i)))):
		nums.append(i)
print(nums, sum(nums))