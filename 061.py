from math import sqrt
from collections import defaultdict
import itertools
# import sys
# sys.setrecursionlimit(100000)
tests = {
	3:lambda x:(sqrt(1+8*x) - 1) / 2,
	4:lambda x:sqrt(x),
	5:lambda x:(sqrt(1+24*x) + 1) / 6,
	6:lambda x:(sqrt(1+8*x) + 1) / 4,
	7:lambda x:(sqrt(9+40*x) + 3) / 10,
	8:lambda x:(sqrt(1+3*x) + 1) / 3,
}


def update_types(old, new):
	singles = [t for t in old if len(t) == 1]
	doubles = [d for t in old for d in t if len(t) == 2]
	if len(new) == 1:
		if new in old:
			return [False]
		else:
			for t in old:
				if len(t) == 2 and new[0] in t:
					t.remove(new[0])
					old = update_types(old, new)
					if old[0]:
						return [True, old[1]]
					else:
						return old
			else:
				old.append(new)
				return [True, old]
	elif len(new) == 2:
		doubles += new
		counts = [doubles.count(d) for d in doubles]
		if len(list(set(counts))) == 1 and 1 not in counts:
			old  = singles + [[n] for n in set(doubles)]
			return [True, old]
		else:
			for t in singles:
				if t[0] in new:
					new.remove(t[0])
					old = update_types(old, new)
					if old[0]:
						return [True, old[1]]
					else:
						return old
			else:
				old.append(new)
				return [True, old]

def findNext(n, num_chain, type_chain, fails, length):
	if len(num_chain) == 6 and str(num_chain[0])[:2] == str(num_chain[-1])[-2:]:
		print(num_chain, sum(num_chain))
	for num in list(nums):
		if num not in fails and num not in num_chain and str(n)[-2:] == str(num)[:2] and num not in num_chain:
			u = update_types(type_chain, nums[num])
			# print(num, u)
			if u != None and u[0]:
				num_chain.append(num)
				if len(num_chain) < length+1:
					return findNext(num, num_chain, u[1],fails, length)
				else:
					return num_chain
	else:
		if len(num_chain) > 1:
			fails.append(n)
			num_chain = num_chain[:-1]
			type_chain = type_chain[:-1]
			return findNext(num_chain[-1], num_chain, type_chain, fails, length)
				

length = 6
nums = {}
for i in range(1000, 10000):
	n = 0
	t = []
	for test, l in tests.items():
		if test < length + 3:
			if l(i) == int(l(i)):
				n = i
				t.append(test)
	if n != 0:
		nums[n] = t

for n in nums:
	# print(n)
	findNext(n, [n], [nums[n]], [], length)
	# print()