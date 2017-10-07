n = 600851475143
def is_prime(x):
	if x % 2 == 0:
		return False
	for i in range(3, int(x ** 0.5) + 1, 2):
		if x % i == 0:
			return False
	return True

def largest_factor(x):
	print(x)
	bound = 7000
	known_primes = [i for i in range(2, bound) if is_prime(i)]
	for prime in known_primes:
		if x % prime == 0:
			if x == prime:
				return x
			print(prime)
			return largest_factor(x // prime)
largest_factor(n)