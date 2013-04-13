import itertools
import tools3

if __name__ == '__main__':
	lst = list(range(9,0,-1))
	perms = itertools.permutations(lst)
	
	for p in perms:
		x = p[0]*1000 + p[1]*100 + p[2]*10 + p[3]
		y = p[4] *10000 + p[5]*1000 + p[6]*100 + p[7]*10 + p[8]

		if tools3.gcd(x,y) == x and y/2 == x:
			print(x*100000+y)
			break