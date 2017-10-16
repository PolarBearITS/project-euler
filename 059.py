import itertools
import enchant
dictionary = enchant.Dict('en_US')
nums = []
with open('059.txt', 'r') as f:
	nums = list(map(int, f.read().split(',')))
for a in range(97, 123):
	for b in range(97, 123):
		for c in range(97, 123):
			key = (a, b, c)
			text = [n ^ key[i % 3] for i, n in enumerate(nums)]
			plain_text = ''.join(map(chr, text))
			words = [w for w in plain_text.split() if dictionary.check(w)]
			if len(words) > 0.5 * len(plain_text.split()):
				print(plain_text)
				print(sum(map(ord, plain_text)), key, ''.join(map(chr, key)))