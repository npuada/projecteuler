import math

if __name__ == '__main__':
	factor_map = {}
	i = 2
	run = 0
	while True:
		for j in range(int(math.floor(math.sqrt(i))), 1, -1):
			if i % j == 0:
				factors = factor_map[j] | factor_map[i/j]
				factor_map[i] = factors	
				break
		else:
			factors = set([i,])
			factor_map[i] = factors	

		if len(factor_map[i]) == 4:
			run += 1
		else:
			run = 0

		if run == 4:
			break

		i += 1
		pass

	print i-3