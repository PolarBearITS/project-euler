i = 1
is_perm = False
while not is_perm:
	i += 1
	print(i)
	mults = [set(str(i * n)) for n in range(1, 7)]
	mults = [l for l in mults if l != mults[0]]
	if len(mults) == 0:
		is_perm = True
print(i)