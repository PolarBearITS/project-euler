triangles = []
origins = []
with open('102.txt') as f:
	for line in f.read().splitlines():
		coords = list(map(int, line.split(',')))
		triangles.append([coords[:2], coords[2:4], coords[4:]])
		origins.append(False)

for i, triangle in enumerate(triangles):
	pass