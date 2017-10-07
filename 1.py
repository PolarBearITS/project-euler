bound = 1000
print(sum(i for i in range(bound) if not(i%3) or not(i%5)))