def reverse(n):
	return int(str(n)[::-1])
def is_palindrome(n):
	return str(n) == str(n)[::-1]
lychrel = []
for n in range(1, 10000):
	iterations = 0
	x = n
	is_lychrel = True
	while iterations < 50:
		x += reverse(x)
		iterations += 1
		if is_palindrome(x):
			is_lychrel = False
			# print(n, x, iterations)
			break
	if is_lychrel:
		lychrel.append(n)
		print(n)
print(lychrel)
print(len(lychrel))