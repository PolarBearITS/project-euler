import itertools
import functools
from operator import mul
limit = 12
for k in range(2, limit+1):
	for combo in sorted(itertools.combinations_with_replacement(range(1, k+1), k), key=sum):
		if sum(combo) == functools.reduce(mul, combo):
			print(combo, sum(combo))
			break


# def bin_to_list(n, k):
# 	return list(map(int, str(bin(n))[2:].zfill(k)))

# def list_sum(a, b):
# 	return list(map(sum, zip(a, b)))


# k = 4
# l = [1]*4
# print(l)
# for i in range(2**k):
# 	print(i, bin_to_list(i, k), list_sum(l, bin_to_list(i, k)))