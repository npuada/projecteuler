#include <stdio.h>

int main()
{	int fibA=0, fibB=1, fibC, temp;
	//int add[25], sum[25], carry=0, i;
	int sum=0;
	/*for(i=0; i<25; i++)
		sum[i]=0, add[i]=0;
	*/
	while(fibC<4000000)
	{
		fibC=fibA+fibB;	
		fibA=fibB;
		fibB=fibC;
		
		if(fibC%2==0)
		{	sum+=fibC;
			printf("%d ", fibC);
		}
		/*{	temp=fibC, i=24;
			while(temp>0)
			{	temp/=10;
				i--;
				printf("%d ", add[i]);
			}
			
			i=24;
			while(i>0)
			{	sum[i]=sum[i]+add[i]+carry;
				if(sum[i]>10)
				{	sum[i]%=10;
					carry=1;
				}
				else
					carry=0;
				i--;
			}
		}*/
	}
	
	/*i=0;
	while(sum[i]=0)
		i++;
		
	for(temp=24;temp>i;temp--)
		printf("%d", sum[temp]);*/
	printf("%d", sum);
	return 0;
}