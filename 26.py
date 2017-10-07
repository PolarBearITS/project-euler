def get_repeating(n):
	value = 1
	mods = []
	while True:
		value %= n
		if value in mods:
			return len(mods)-mods.index(value)
		mods.append(value)
		value *= 10

cycles = {i:get_repeating(i) for i in range(1, 1000)}
print([(k, v) for k, v in cycles.items() if v == max(cycles.values())])