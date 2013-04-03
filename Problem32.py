import itertools

def toList(num):
	digits = []

	while num > 0:
		digits.append(num%10)
		num //= 10

	return digits

if __name__ == '__main__':
	digits = [i for i in range(1,10)]
	pandigital_product = []

	perms = itertools.permutations(digits,5)
	for p in perms:
		tmp = p[:3]
		x1 = 100*tmp[0] + 10*tmp[1] + tmp[2]
		tmp = p[3:]
		y1 = 10*tmp[0] + tmp[1]

		product = x1*y1
		product_list = toList(product)
		digit_count = [0 for i in range(10)]

		for digit in list(p)+product_list:
			digit_count[digit] += 1

		for count in digit_count[1:]:
			if count != 1:
				break
		else:
			if digit_count[0] == 0:
				if product not in pandigital_product:
					pandigital_product.append(product)

		tmp = p[1:]
		y2 = 1000*tmp[0] + 100*tmp[1] + 10*tmp[2] + tmp[3]
		x2 = p[0]

		product = x2*y2
		product_list = toList(product)
		digit_count = [0 for i in range(10)]

		for digit in list(p)+product_list:
			digit_count[digit] += 1

		for count in digit_count[1:]:
			if count != 1:
				break
		else:
			if digit_count[0] == 0:
				if product not in pandigital_product:
					pandigital_product.append(product)

	print(sum(pandigital_product))

