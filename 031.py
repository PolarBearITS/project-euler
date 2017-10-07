
def coin_sum(n):
	coins = [1, 2, 5, 10, 20, 50, 100, 200]
	sums = {k:v for k, v in zip(range(1, n+1), [0]*n)}
	for coin in coins:
		for value in sums:
			if value == coin:
				sums[value] += 1
			elif value > coin:
				sums[value] += sums[value-coin]
	print(sums[n])
coin_sum(200)