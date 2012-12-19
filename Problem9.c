#include <stdio.h>
#include <math.h>

void isSum1000(int a, int b)
{
	int c, k=1;
	int aTemp, bTemp;

	do {
		aTemp = k*a;
		bTemp = k*b;
		c = (int)sqrt(aTemp*aTemp + bTemp*bTemp);
		k++;
	} while(aTemp + bTemp + c < 1000);

	if(aTemp + bTemp + c == 1000)
		printf("%d %d %d", aTemp, bTemp, c);
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

int main()
{
	int m = 2, n = 1;
	int a = 0, b = 0;
	
	while(a + b < 600)
	{
		while(n < m)
		{	
			if(gcd(m, n) == 1)
			{	a = m*m - n*n;
				b = 2 * m * n;

				isSum1000(a, b);
				//printf("%4d %4d\n", a, b);
			}
			n+=2;
		}

		m++;
		n = m%2 == 0 ? 1 : 2;
	}
}
