def value(hand):
	values = {
		'T':10,
		'J':11,
		'Q':12,
		'K':13,
		'A':14,
	}
	hand_type = 0
	hand_num = [0]
	high_num = 0
	nums = []
	suits = []
	for card in hand:
		num = card[0]
		suit = card[1]
		if num in values:
			num = values[num]
		else:
			num = int(num)
		nums.append(num)
		suits.append(suit)

	# high value
	hand_type = 1
	hand_num = [max(nums)]
	high_num = sorted(nums, reverse=True)

	# combo
	pairs = [x for x in nums if nums.count(x) >= 2]
	if len(pairs) == 2:
		hand_type = 2
		hand_num = [pairs[0]]
	elif len(pairs) == 4:
		if pairs.count(pairs[0]) != 4:
			hand_type = 3
			hand_num = list(set(pairs))
		else:
			hand_type = 8
			hand_num = list(set(pairs))
			print(hand)
	elif len(pairs) == 3:
		hand_type = 4
		hand_num = list(set(pairs))
	elif len(pairs) == 5:
		hand_type = 7
		hand_num = list(set(pairs))

	# order
	order = sorted(nums)
	ordered_suits = list(set(suits))
	is_straight = False
	is_flush = False
	#straight
	if len(pairs) == 0 and order[-1] - order[0] == 4:
		hand_type = 5
		hand_num = [order[0]]
	if len(ordered_suits) == 1:
		hand_type = 6
		hand_num = [max(nums)]
	if is_straight and is_flush:
		if nums[0] != 10:
			hand_type = 9
			hand_num = nums[0]
		else:
			hand_type = 10
			hand_num = nums[0]
	return hand_type, hand_num + high_num

def compare_hands(hand1, hand2):
	p1_win = False
	if hand1[0] > hand2[0]:
		p1_win = True
	elif hand1[0] == hand2[0]:
		for i in range(len(hand1[1])):
			if hand1[1][i] > hand2[1][i]:
				p1_win = True
				break
			else:
				break
	return p1_win


hands = []
with open('054.txt', 'r') as f:
	hands = [l.split() for l in f.read().split('\n')[:-1]]
wins = 0
for hand in hands:
	p1 = hand[:5]
	p2 = hand[5:]
	h1 = value(p1)
	h2 = value(p2)
	w = compare_hands(h1, h2)
	print(p1, p2, h1[0], h2[0], w)
	if w:
		wins += 1
print(wins)