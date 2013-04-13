import itertools
import tools3

primes = tools3.getPrimes(2766)
primes.reverse()

if __name__ == '__main__':
	for p in itertools.permutations(reversed(range(1,8))):
		if p[6] %2 == 1:
			num = p[0]*1000000 + p[1]*100000 + p[2]*10000 + p[3]*1000 + p[4]*100 + p[5]*10 + p[6]
			for p in primes:
				if num%p == 0:
					break
			else:
				print(num)
				break