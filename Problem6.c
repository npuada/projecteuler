#include <stdio.h>
#include <math.h>

int main()
{
	//int squareOfSum = (int)(pow(100,4) + 2*pow(100,3) + pow(100,2))/4;
	int squareOfSum = 0;
	int sumOfSquares = 0;

	int i = 1;
	
	for(; i<= 100; i++)
		sumOfSquares += i*i;

	for(i = 1; i <= 100; i++)
		squareOfSum += i;

	squareOfSum = (int)(pow(squareOfSum,2));
	printf("%d", squareOfSum - sumOfSquares);

	return 0;
}
