#include <stdio.h>

int is6DigitPalindrome(int x)
{	int x1=x/1000, x2=x%1000;

	if(x1/100 == x2%10 && x1%10 == x2/100 && (x1/10)%10 == (x2/10)%10)
		return 1;
	else
		return 0;
}

int main()
{	int x1=999, x2=x1;
	int largestPalindrome=0, temp;
	
	while(x1*x2>100000 && x1>500)
	{	temp=x1*x2;
		if(is6DigitPalindrome(temp)==1 && temp>largestPalindrome)
			largestPalindrome=temp;
		x2--;
		if(x1*x2<=100000)
		{	x2=999;
			x1--;
		}
	}
	
	printf("%d", largestPalindrome);
	
	return 0;
}