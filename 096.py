# import numpy
from copy import deepcopy
grids = []
with open('096.txt') as f:
	grid = []
	for line in [l.strip('\n') for l in f.readlines()]:
		if 'Grid' in line:
			grid = []
		else:
			grid.append(list(map(int, line)))
		if len(grid) == 9:
			grids.append(grid)

def check(grid, columns, squares):
	for row in grid:
		if set(row) != set(range(1, 10)):
			return False

	for col in columns:
		if set(col) != set(range(1, 10)):
			return False

	for sq in squares:
		if set(sq) != set(range(1, 10)):
			return False

	return True


def eliminate(grid, poss):
	ng = deepcopy(grid)
	# p = [list(map(len, row)) for row in poss]
	pcol = get_cols(poss)
	psquares = get_squares(poss)
	# display((p, pcol, psquares))

	# Naked Cells
	for i, row in enumerate(poss):
		for j, col in enumerate(row):
			if len(col) == 1:
				ng[i][j] = list(col)[0]

	#rows
	for i, row in enumerate(poss):
		for j, col in enumerate(row):
			for l in col:
				indexes = [k for k, search in enumerate(row) if l in search]
				if len(indexes) == 1:
					ng[i][j] = l
				elif len(set(index//3 for index in indexes)) <= 1:
					for a in range(3*(i//3), 3*(i//3 + 1)):
						for b in range(3*(j//3), 3*(j//3 + 1)):
							if (a != i or b not in indexes) and l in poss[a][b]:
								poss[a][b].remove(l)

	# #cols
	for j, col in enumerate(pcol):
		for i, row in enumerate(col):
			for l in row:
				indexes = [k for k, search in enumerate(col) if l in search]
				if len(indexes) == 1:
					ng[i][j] = l
				elif len(set(index//3 for index in indexes)) <= 1:
					for a in range(3*(i//3), 3*(i//3 + 1)):
						for b in range(3*(j//3), 3*(j//3 + 1)):
							if (a not in indexes or b != j) and l in poss[a][b]:
								poss[a][b].remove(l)

	#squares
	for a, bsq in enumerate(psquares):
		for b, lsq in enumerate(bsq):
			for l in lsq:
				if sum(int(l in x) for x in bsq) == 1:
					ng[3*(a//3)+b//3][3*(a%3)+b%3] = l

	return ng

			

def solve(grid):
	g = deepcopy(grid)
	steps = 0
	while True:
		cols = get_cols(g)
		squares = get_squares(g)
		possibles = [[{}]*len(g) for _ in range(len(g))]
		for i in range(len(g)):
			for j in range(len(g)):
				square = 3*(i//3)+j//3
				if g[i][j] == 0:
					p = set(range(1, 10))
					for l in g[i] + cols[j] + squares[square]:
						if l in p:
							p.remove(l)
					possibles[i][j] = p
		newG = eliminate(g, possibles)
		# display((g, newG, possibles))
		if newG == g:
			break
		g = newG
		steps += 1
	return newG, possibles, check(newG, cols, squares), steps
	


def get_cols(grid):
	return list(map(list, zip(*grid)))

def get_squares(grid):
	squares = []
	for i in range(len(grid)):
		sq = []
		for j in range(len(grid)):
			sq.append(grid[3*(i//3)+j//3][3*(i%3)+j%3])
		squares.append(sq)
	return squares


def display(grids):
	for rows in zip(*grids):#numpy.array(grid):
		for row in rows:
			print(row, end= ' ')
		print()
	print()

total = 0
for i, grid in enumerate(grids):
	new_grid, possibles, solved, steps = solve(grid)
	print(f'Grid {i} - {steps} steps', solved)
	if solved:
		total += 1
	if not solved:
		print(grid)
		# break
	# print(steps, solved)
print(total)
