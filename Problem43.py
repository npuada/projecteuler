#!C:/Python33/python.exe -u
import itertools

def to_num(tup):
	powTen = 1
	num = 0
	for t in tup[::-1]:
		num  += (t*powTen)
		powTen *= 10

	return num

if __name__ == '__main__':
	interesting = []
	primes = [2, 3, 5, 7, 11, 13, 17]
	
	perms = itertools.permutations(range(10))
	skip = None
	start = 0
	for p in perms:
		if p[start:start+3] == skip:
			continue
		else:
			skip = None
			start = 0

		for i in range(1,8):
			digits = p[i:i+3]
			num = to_num(digits)

			if num % primes[i-1] != 0:
				skip = digits
				start = i
				break
		else:
			interesting.append(to_num(p))

	print(sum(interesting))