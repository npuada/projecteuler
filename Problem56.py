import math

def getDigitSum(num):
	digit_sum = 0
	while num > 0:
		digit_sum += (num%10)
		num //= 10
	return digit_sum

if __name__ == '__main__':
	a = 99
	b = 99
	power = a**b
	max_sum = getDigitSum(power)

	while a >= 11:
		b = 99
		for b in range(100,1,-1):
			power = a**b
			digit_sum = getDigitSum(power)
			if digit_sum > max_sum:
				max_sum = digit_sum
				pair = a,b

			if math.floor(math.log(power))*9 < max_sum:
				break
		a -= 1

	print('Sum of digits of ', pair[0], '^', pair[1], ' is ', max_sum, sep='')
