#include <stdio.h>

int main() {
	int sum = 1, i = 2, j, temp = 1;

	for(i; i <= 1000; i+=2)
		for(j = 0; j < 4; j++) {
			temp += i;
			sum += temp;
		}
			
	printf("%d", sum);
	return 0;
}
