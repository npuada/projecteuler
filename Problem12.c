#include <stdio.h>

int main()
{
	int i = 1, temp = 2, count = 0;
	
	while(i < 10000)
	{
		count = 0;
		i++;
		
		printf("%d ", i);
		int j, temp = 1;
		for(j = i; j > temp; j--)
		{	if(i%j == 0)
			{	count +=2;
				temp = i/j;
				printf("[%d * %d] ", i/j, j);
			}
		}

		printf("%d\n\n", count);
	}

	return 0;
}
