lens = {
	1:31,
	2:28,
	3:31,
	4:30,
	5:31,
	6:30,
	7:31,
	8:31,
	9:30,
	10:31,
	11:30,
	12:31,
}

year = 1900
month = 1
date = 1
day = 1
count = 0

while year != 2001:
	if (year % 4 == 0) and (year % 400 not in [100, 200, 300]):
		lens[2] = 29
	else:
		lens[2] = 28
	day += 1
	day %= 7
	if day == 0 and date == 1 and year > 1900:
		count += 1
	date += 1
	if date > lens[month]:
		month += 1
		date = 1
	if month > 12:
		year += 1
		month -= 12
print(count)