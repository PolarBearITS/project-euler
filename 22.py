names = []
with open('22.txt') as f:
	names = sorted(f.read().replace('"', '').split(','))

print(sum((i+1)*sum(ord(c)-64 for c in name) for i, name in enumerate(names)))