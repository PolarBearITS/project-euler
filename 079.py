from collections import defaultdict

nums = [list(map(int, line)) for line in open('079.txt').read().splitlines()]

order = defaultdict(list)
for x in range(10):
	for num in nums:
		for i, n in enumerate(num):
			if n == x:
				order[x] += []
				if i > 0:
					for k in num[:i]:
						if k not in order[x]:
							order[x].append(k)

password = ''
while len(order) != 0:
	for n, o in order.items():
		if o == []:
			password += str(n)
			order = {k:[val for val in v if val != n] for k, v in order.items() if k != n}
			break

print(password)