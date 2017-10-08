def map_alpha(c):
	return ord(c)-64

t = ''
triangles = [i*(i+1)//2 for i in range(1, 27)]
with open('042.txt', 'r') as f:
	t = f.read().replace('"', '').split(',')
n = 0
for word in t:
	if sum(map(map_alpha, word)) in triangles:
		n += 1
		print(word)
print(n)