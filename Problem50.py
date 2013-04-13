import tools3

SIZE = 4999
primes_1m = tools3.getPrimes(1000000)
primes = primes_1m[1:SIZE+1]

lookup = {}
for p in primes_1m:
	lookup[p] = True

if __name__ == '__main__':
	sum_matrix = []
	row = primes
	
	index = 0
	length = 3
	max_prime = (0, length)
	#SIZE-2 sums of length 3, SIZE-4 sums of length 5, etc. 
	for i in range(SIZE-2, 0, -2):
		tmp = []
		#do not include first and last element
		for j in range(1, i+1):
			seq_sum = row[j] + primes[j-1] + primes[j+(SIZE-i)-1]
			if lookup.get(seq_sum):
				if seq_sum > max_prime[0] or length > max_prime[1]:
					max_prime = seq_sum, length
			tmp.append(seq_sum)
		row = tmp
		if row[0] > 1000000:
			break
		index += 1
		length += 2

	print(max_prime)
