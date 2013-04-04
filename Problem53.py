if __name__ == '__main__':
	n = 23
	r = 1
	total = 0
	while n <= 100:
		combi = 0
		num = 1
		den = 1
		count = 0
		i = n
		j = r
		while combi < 1000000 and j < i:
			num *= i
			den *= j
			combi = num//den
			if combi < 1000000:
				count += 1
			i -= 1
			j += 1
		total += (n - (2*count+1))
		n += 1

	print(total)