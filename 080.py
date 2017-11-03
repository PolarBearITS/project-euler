import math
from decimal import *
limit = 100
getcontext().prec = limit * 3//2
irrs = sorted(list(set(range(limit + 1)) - set([n**2 for n in range(int(math.sqrt(limit) + 1))])))

def sq(n, prec):
	x = Decimal(math.sqrt(n))
	old = Decimal(1/3)
	while str(x)[2:2 + prec] != str(old)[2:2 + prec]:
		old = x
		a = (Decimal(n)-Decimal(x**2))/Decimal(2*x)
		b = Decimal(x + a)
		x = b - Decimal((a**2)/(2*b))
	return x

m = 0
for i in irrs:
	m += sum(map(int, str(sq(i, limit)).replace('.', '')[:limit]))
print(m)
