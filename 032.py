import itertools
pandigits = []
products = []
for i, j in itertools.product(range(1, 5000), range(1, 5000)):
	x = i*j
	if x > 10000:
		continue
	p = str(i)+str(j)+str(x)
	if len(p) == 9:
		if x not in pandigits:
			if all(d in p for d in map(str, range(1, 10))):
				print(f'{i} * {j} = {x}')
				pandigits.append(x)
print(pandigits, sum(pandigits))