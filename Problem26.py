#30872nd
import tools

def multiplicative_order(a,n):
	base = a
	for i in range(1,n):
		if a % n == 1:
			return i
		a *= base

if __name__ == "__main__":
	max = (0,0)

	for i in range(2,1000):
		if tools.gcd(i,10) == 1:
			x = multiplicative_order(10,i)
			if x > max[1]:
				max = (x,i)

	print max