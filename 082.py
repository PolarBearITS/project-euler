import math
from collections import defaultdict
matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]

nodes = defaultdict(list)
for i in range(len(matrix)):
	for j in range(len(matrix)):
		n = matrix[i][j]
		if j == 0:
			nodes[0].append(n)
			nodes[n].append(matrix[i][j+1])
		elif j == len(matrix)-1:
			nodes[math.inf].append(n)
			nodes[n].append(matrix[i][j-1])
		else:
			if i > 0:
				nodes[n].append(matrix[i-1][j])
			if i < len(matrix)-1:
				nodes[n].append(matrix[i+1][j])
			nodes[n].append(matrix[i][j+1])


print(nodes)