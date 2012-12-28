#33491st
from math import floor, sqrt,log
import primes

def rotate(n):
	powTen = int(10**(floor(log(n, 10))))
	rotations = []
	init = (n%powTen*10 + n/powTen)
	rotations.append(init)
	while init != n:
		init = (init%powTen*10 + init/powTen)
		rotations.append(init)

	return rotations

def getCircularPrimes(primeList):
	circularPrimes = [2, 5,]
	for p in primeList:
		rotations = rotate(p)
		if all(i%2 == 1 and i%5 != 0 for i in rotations):
			if all(i in primeList for i in rotations):
				for j in rotations:
					circularPrimes.append(j)

	return circularPrimes

if __name__ == '__main__':
	circularPrimes = getCircularPrimes(primes.getPrimes(1000000))
	print len(set(circularPrimes))