def spiral_center_diagonal_sum(n):
	squares = [i**2 for i in range(1, n+1) if i % 2]
	gap = 0
	k = 1
	s = 0
	while k < n**2:
		k += gap
		s += k
		if k in squares:
			gap += 2
	return s

print(spiral_center_diagonal_sum(1001))