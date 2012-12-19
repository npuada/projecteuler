#include <stdio.h>

int main()
{
	int i=3, sum=i;
	
	while(i<999)
	{
		i++;
		if(i%5==0 || i%3==0)
			sum+=i;\
		
		//else if((i-1)%5==0 || (i-1)%3==0)
		//sum+=(i-1);
	}
	
	printf("%d", sum);
}