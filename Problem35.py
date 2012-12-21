#33491st
from math import floor, sqrt,log

def getPrimes(limit):
	if limit < 2:
		return []

	odd = [i for i in range(3, limit, 2)]
	primeMap = {i: True for i in odd}
	
	primeList = [2]
	stop = floor(sqrt(max(odd)))
	for i in odd:
		key = i**2
		while key < limit:
			primeMap[key] = False
			key += (i*2)
		if i > stop:
			break

	for key in primeMap:
		if primeMap[key]:
			primeList.append(key)
	return primeList

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
	circularPrimes = getCircularPrimes(getPrimes(1000000))
	print set(circularPrimes)
	print len(set(circularPrimes))