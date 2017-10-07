import itertools
i = 1
for p in itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10):
	if i == 1000000:
		print(''.join(map(str, p)))
		break
	i += 1