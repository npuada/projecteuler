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

def gcd(a,b):
	if a == 0 or b == 0:
		return abs(a-b)

	while a != 0 and b != 0:
		if a > b:
			a %= b
		elif b >= a:
			b %= a

	if a > b:
		return a
	else:
		return b