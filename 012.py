import functools
def triangle(n):
	return n*(n+1)//2

def factors(n):    
    return set(functools.reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

i = 1
while len(factors(triangle(i))) < 500:
	i += 1
	print(i, triangle(i))