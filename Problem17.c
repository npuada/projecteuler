#include <stdio.h>

int lessThanTwenty[19]={3, 3, 5, 4, 4, 3, 5, 5, 4, 3,
						6, 6, 8, 8, 7, 7, 9, 8, 8};
int multipleOfTen[8] = {6, 6, 5, 5, 5, 7, 6, 6};


int lessThan20(int i) {
	return lessThanTwenty[i-1];
}

int lessThan100(int i) {
	int sum = 0, temp = i/10;
	if(i >= 20) {
		if(temp > 0)
			sum = multipleOfTen[temp-2];
		temp = i%10;
		if(temp > 0)
			sum += lessThanTwenty[temp-1];
	}
	else
		sum = lessThanTwenty[i-1];
	return sum;
}

int lessThan1000(int i) {
	int sum = 0, temp = i/100;
	sum = lessThanTwenty[temp-1] + 10;
	temp = i%100;
	sum += lessThan100(temp);

	return sum;
}

int main() {
	int i, sum=0;
	for(i = 1; i < 1000; i++)
	{
		if(i < 20) {
			sum += lessThan20(i);
		}
		else if(i < 100){
			sum += lessThan100(i);
		}
		else {
			if(i%100 != 0)
				sum += lessThan1000(i);
			else
				sum = sum + lessThanTwenty[i/100 - 1] + 7;		
		}
	}

	printf("%d", sum+11);

	return 0;
}
