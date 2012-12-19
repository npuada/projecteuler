pow_list = [i**5 for i in range(0,10)]
total = 0

for i in range (4000, 295245):
	if 1000 < i < 10000:
		pow_ten = 1000
	elif 10000 < i < 100000:
		pow_ten = 10000
	else:
		pow_ten = 100000

	sum = 0
	while pow_ten >= 1:
		digit = i / pow_ten
		digit %= 10
		sum += pow_list[digit]
		pow_ten /= 10

	if sum == i:
		total += sum

print total
