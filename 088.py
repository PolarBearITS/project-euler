import itertools
limit = 6
for k in range(2, limit+1):
	for combo in itertools.combinations_with_replacement(range(1, k+1), k):
		m = 1
		for c in combo:
			m *= c
		if sum(combo) == m:
			print(m, combo)
			break