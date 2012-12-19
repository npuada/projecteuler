#define MAX 3
#include <stdio.h>

int main() {
	int a[MAX] = {0};
	int b[MAX] = {0};
	int c[MAX] = {0};
	//int temp[125];
	
	int i,j;
	a[0] = 1;
	b[0] = 1;
	while(c[MAX-1] == 0) {
		i = 0;
		do {
			c[i] = a[i]+b[i];
			if(c[i] > 1000000000) {
				c[i] %= 1000000000;
				c[i+1] = c[i+1] + c[i]/1000000000;
			}
			printf("%d", i);
			i++;
		} while(c[i] > 0);
		
		for(j = 0; j < 125; j++) {
			a[j] = b[j];
		}
		for(j = 0; j < 125; j++) {
			b[j] = c[j];
		}
	}

	for(i=124; i >= 0; i--)
		printf("%d ", c[i]);
	return 0;
}