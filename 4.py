import math
def is_palindrome(n):
	return str(n) == str(n)[::-1]

m = 0
for i in range(999, 99, -1):
	for j in range(999, 99, -1):
		p = i * j
		if p > m:
			if is_palindrome(p):
				m = p
				print(m, i, j)
print(m)