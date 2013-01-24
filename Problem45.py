#29601st
def pentagonal(n):
	return (n * (3*n-1))/2

def hexagonal(n):
	return (n * (2*n-1))

if __name__ == '__main__':
	tri_list = []
	p_list = [1,]
	h_list = [1,]
	x = 2
	y = 2
	while True:
		h_max = h_list[len(h_list)-1]

		p = pentagonal(x)
		p_list.append(p)
		while p <= h_max:
			x += 1
			p = pentagonal(x)
			p_list.append(p)
			if p == h_max:
				print p

		p_max = p_list[len(p_list)-1]
		h = hexagonal(y)
		h_list.append(h)
		while h <= p_max:
			y += 1
			h = hexagonal(y)
			h_list.append(h)
			if h == p_max:
				print h
