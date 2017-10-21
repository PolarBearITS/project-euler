nums = []
for i in range(1, 100):
	n = 1
	while len(str(n ** i)) < i + 1:
		if len(str(n ** i)) == i:
			nums.append(n ** i)
			print(n ** i, f'= {n} ^ {i}')
		n += 1
print(len(nums))