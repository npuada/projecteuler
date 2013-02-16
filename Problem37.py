import math
import tools

primes = tools.getPrimes(800000)
primes.sort()

def is_prime(n):
	if n == 1:
		return False

	if n in primes:
		return True
	return False

def left_truncatable(n):
	while n > 0:
		if not is_prime(n):
			return False
		n /= 10
	return True

def right_truncatable(n):
	q = 10
	while q < n:
		if not is_prime(n%q):
			return False
		q *= 10
	return True

if __name__ == "__main__":
	start37 = primes[4:25]
	
	powTen = 1
	over100 = primes[25:]
	for p in over100:
		tmp = p
		if powTen < p/10:
			powTen *= 10
		if (tmp/powTen == 3 or tmp/powTen == 7) and (tmp%10 == 3 or tmp%10 == 7):
			while tmp > 0:
				if tmp%2 == 0 or tmp%5 == 0:
					break
				if tmp == 9 or tmp == 1:
					break
				tmp /= 10
			if tmp == 0:
				start37.append(p)

	total = 0
	for p in start37:
		if right_truncatable(p):
			if left_truncatable(p):
				total += p
	print total
