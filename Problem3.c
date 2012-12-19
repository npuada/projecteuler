#include <stdio.h>
#include <math.h>

int isPrime(int x)
{	int i=(int)floor(sqrt(x));

	while(x%i!=0 && i>1)
		i--;
		
	if(i==1)
		return 1;
	else
		return 0;
}

int main()
{	long long comp=600851475143LL, sqrRoot;
	int pFactor, temp=3;
	
	sqrRoot=(long long)ceil(sqrt(comp));
	pFactor=sqrRoot;
	
	while(temp<sqrRoot)
	{	if(isPrime(temp)==1 && comp%temp==0)
			pFactor=temp;
			
		temp++;
	}
	
	printf("%d",pFactor);
	return 0;
}