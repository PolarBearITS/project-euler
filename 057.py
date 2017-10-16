n = 0
d = 1
l = 0
for i in range(1000):
	temp = n
	n = d
	d = 2*d + temp
	if len(str(n + d)) > len(str(d)):
		l += 1
		print(i)
print(l)