matrix = [list(map(int, line.split(','))) for line in open('081.txt').read().splitlines()]

def make_pyramid(m):
	N = len(m)
	pyramid = []
	for i in range(2*N-1):
		row = []
		for j in range(max(0, i-N+1), min(i+1, N)):
			row.append(m[j][i-j])
		e = (i+1-len(row))//2
		row = [0]*e + row + [0]*e
		pyramid.append(row)
	return pyramid

triangle = make_pyramid(matrix)[::-1]
for i in range(1, len(triangle)):
	pairs = [triangle[i-1][j:j+2] for j in range(len(triangle[i]))]
	new = []
	for pair in pairs:
		if 0 in pair:
			new.append(max(pair))
		else:
			new.append(min(pair))
	triangle[i] = [x + y for x, y in zip(triangle[i], new)]
print(triangle[-1][0])