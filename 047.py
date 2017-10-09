def factors(n):
	i = 2
	f = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			f.append(i)
	if n > 1:
		f.append(n)
	return f

is_cons = False
i = 1
while not is_cons:
	i += 1
	cons_factors = []
	for x in range(i, i+4):
		cons_factors += list(set(factors(x)))
	print(range(i, i+4), len(cons_factors), cons_factors)
	if len(cons_factors) == 16:
		print(i)
		is_cons = True