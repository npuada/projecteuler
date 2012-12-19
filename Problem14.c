#include <stdio.h>

int main()
{
	unsigned long long i, run = 2LL;
	int step, curr = 2, max=1;

	while(run < 1e6)
	{
		i = run, step = 1;	
		while(i != 1)
		{
			if(i%2)
				i = i*3 + 1;
			else
				i /= 2;
			step++;
		}

		printf("%llu %d\n", run, step);
		if(step > max)
			max = (int)run;

		run++;
	}

	printf("%d", max);

	return 0;
}
