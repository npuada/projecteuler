import math

def is_prime(num):
	if num%2 == 0:
		if num != 2:
			return False
		else:
			return True
	elif num%5 == 0 or num == 1:
		return False

	up = math.floor(math.sqrt(num))
	up += 1 if up%2 == 0 else 0	
	for i in range(up, 2, -2):
		if num%i == 0:
			return False
	else:
		return True

if __name__ == '__main__':
	squares = [0, 1, 4]
	next_square = 3
	i = 9
	while True:
		if is_prime(i):
			i += 2
			continue

		if i > (2*squares[-1:][0]) + 1:
			squares.append(next_square**2)
			next_square += 1

		for j in squares[::-1]:
			if 2*j < i:
				addend = i - 2*j
				if is_prime(addend):
					break
		else:
			print(i)
			break

		i += 2