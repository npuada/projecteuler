import math

def getPrimes(limit):
	if limit < 2:
		return []

	odd = [i for i in range(3, limit, 2)]
	primeMap = {i: True for i in odd}
	
	primeList = [2]
	stop = math.floor(math.sqrt(max(odd)))
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
