from math import sqrt
from collections import defaultdict
def squares(word):
	length = len(word)
	sq = []
	uniques = defaultdict(list)
	for i, c in enumerate(word):
		uniques[c].append(i)
	for n in range(int(sqrt(10**(length-1))), int(sqrt(10**length))+1):
		s = n**2
		unique_nums = defaultdict(list)
		for i, c in enumerate(str(s)):
			unique_nums[c].append(i)
		if list(uniques.values()) == list(unique_nums.values()):
			sq.append(s)
	return sq

def anagram_num(anagram_map, i):
	j = ['']*len(str(i))
	for n, a in anagram_map.items():
		j[a] = str(i)[n]
	j = int(''.join(j))
	return j

m = 0
words = [word.strip('"') for word in open('098.txt').read().split(',')]
for i, w1 in enumerate(words):
	for j, w2 in enumerate(words[i+1:]):
		if sorted(w1) == sorted(w2):
			sq = squares(w1)
			anagram_map = {}
			for i, c1 in enumerate(w1):
				for j, c2 in enumerate(w2):
					if c1 == c2 and j not in list(anagram_map.values()):
						anagram_map[i] = j
			for s1 in sq:
				s2 = anagram_num(anagram_map, s1)
				if s2 in sq:
					print(w1, w2, s1, s2)
					n = max(s1, s2)
					if n > m:
						m = n
print(m)