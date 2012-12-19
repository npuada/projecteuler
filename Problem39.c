#include <stdio.h>
#include <math.h>

int getSum(int a, int b, int k)
{
	int c;
	int aTemp, bTemp;

	a *= k;
	b *= k;
	c = (int)sqrt(a*a + b*b);
	
	return a+b+c;
}

int gcd(int m, int n)
{	if(m == 0)
		return n;
	while(n != 0)
	{	if(m > n)
			m -= n;
		else
			n -= m;
	}

	return m;
}

int main() {
	int m = 2, n = 1;
	int a = 0, b = 0;
	int solutions[1001];
	
	int i;
	for(i=0; i<1001; i++)
		solutions[i] = 0;

	while(a + b < 600)
	{
		while(n < m)
		{	
			if(gcd(m, n) == 1)
			{	a = m*m - n*n;
				b = 2 * m * n;

				int k = 1, temp;
				do {
					temp = getSum(a, b, k);
					if(temp <= 1000)
						solutions[temp]++;
					k++;
				} while(temp <= 1000);
				//printf("%4d %4d\n", a, b);
			}
			n+=2;
		}

		m++;
		n = m%2 == 0 ? 1 : 2;
	}

	printf("%d", solutions[121]);
	return 0;
}
