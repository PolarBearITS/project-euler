pyramid = open('067.txt', 'r').read()
triangle = [list(map(int,row.split())) for row in pyramid.split('\n')][::-1]
for i in range(1, len(triangle)):
	row = triangle[i]
	pairs = [triangle[i-1][j:j+2] for j in range(len(row))]
	triangle[i] = [x + y for x, y in zip(row, map(max, pairs))]
print(triangle[-1][0])