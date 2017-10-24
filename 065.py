num = 100
length = num - 1
c = [x for f in ((1, 2*k, 1) for k in range(1, length//3 + 2)) for x in f][:length]
n = 0
d = 1
for s in c[::-1]:
	temp = n
	n = d
	d = d*s + temp
print(n + 2*d, d, 2 + n / d)
print(sum(map(int, str(n + 2*d))))