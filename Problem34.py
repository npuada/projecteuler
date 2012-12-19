def fact(x):
	product = 1
	for i in range(1,x+1):
		product *= i
	return product

fact_list = [fact(i) for i in range(0,10)]
total = 0

print fact_list
for i in range (100, 2177280):
	if 100 <= i < 1000:
		pow_ten = 100
	elif 1000 <= i < 10000:
		pow_ten = 1000
	elif 10000 <= i < 100000:
		pow_ten = 10000
	elif 100000 <= i < 1000000:
		pow_ten = 100000
	else:
		pow_ten = 1000000

	sum = 0
	while pow_ten >= 1:
		digit = i / pow_ten
		digit %= 10
		#print"%d %d" % (digit, i)
		sum += fact_list[digit]
		pow_ten /= 10

	if sum == i:
		print i
		total += i

print total
