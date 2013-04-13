import math

def reverse(num):
	rev = 0
	
	tmp = num//10
	powTen = 1
	while tmp > 0:
		tmp //= 10
		powTen *= 10

	while num > 0:
		tmp = num % 10
		rev += (tmp * powTen)
		powTen //= 10
		num //= 10

	return rev

def is_palindrome(num):
	if reverse(num) == num:
		return True
	else:
		return False

if __name__ == '__main__':
	lychrel = []
	for i in range(1, 10000):
		num = i
		for j in range(25):
			rev = reverse(num)
			num += rev
			if is_palindrome(num):
				break
		else:
			lychrel.append(i)

	print(len(lychrel))