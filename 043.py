import itertools
primes = [2, 3, 5, 7, 11, 13, 17]
divisibles = []
for n in itertools.permutations(range(0, 10), 10):
	n = ''.join(map(str, n))
	if all(int(n[i:i+3]) % primes[i-1] == 0 for i in range(1, 8)):
		print(n)
		divisibles.append(int(n))
print(sum(divisibles))