numerals = {
	'I':1,
	'IV':4,
	'V':5,
	'IX':9,
	'X':10,
	'XL':40,
	'L':50,
	'XC':90,
	'C':100,
	'CD':400,
	'D':500,
	'CM':900,
	'M':1000,
}

def get_value(num):
	vals = [numerals[n] for n in num]
	v = 0
	i = 0
	while i < len(vals):
		if i < len(vals) - 1:
			if vals[i+1] > vals[i]:
				v += vals[i+1]-vals[i]
				i += 2
				continue
		v += vals[i]
		i += 1
	return v

def get_numerals(n):
	s = ''
	o = n
	for n, v in reversed(list(numerals.items())):
		while o >= v:
			o -= v
			s += n
	return s


nums = open('089.txt').read().splitlines()
count = 0
for num in nums:
	v = get_value(num)
	nv = get_numerals(v)
	if len(num) != len(nv):
		count += len(num) - len(nv)
print(count)