#32461st
import primes

prime_list = primes.getPrimes(100000)

def isPrime(x):
	index = 0
	while prime_list[index] <= x and index < len(prime_list):
		if prime_list[index] == x:
			return True
		index += 1
	return False

if __name__ == '__main__':
	max = 0
	coefficient_tuple = (0,0)
	for a in xrange(-999,1000,2):
		for b in xrange(-999,1000,2):
			if 1521 + b < a*39:
				break
			x = 0
			while isPrime(x**2 + a*x + b):
				x += 1
			if x > max:
				max = x
				coefficient_tuple = (a,b)

	print max
	print coefficient_tuple
	print coefficient_tuple[0] * coefficient_tuple[1]	