import itertools
import tools

def getDigits(num):
	powTen = 1000
	digits = []
	while powTen > 0:
		tmp = num/powTen
		digits.append(tmp)
		num %= powTen
		powTen /= 10

	return digits

def toNum(tup):
	return 1000*tup[0] + 100*tup[1] + 10*tup[2] + tup[3]

if __name__ == '__main__':
	primes = sorted(tools.getPrimes(10000))
	primes = primes[168:]
	candidates = []
	done = []
	for prime in primes:
		prime_perms = []
		if prime in done:
			continue
		else:
			digits = getDigits(prime)
			for perm in itertools.permutations(digits):
				num = toNum(perm)
				if num in primes and num not in done:
					prime_perms.append(num)
					done.append(num)

		if len(prime_perms) >= 3:
			candidates.append(sorted(prime_perms))

	for lst in candidates:
		for i in range(len(lst)-2):
			for j in range(i+1, len(lst)-1):
				interval = lst[j] - lst[i]
				if lst[j]+interval in lst:
					print lst[i], lst[j], lst[j]+interval
