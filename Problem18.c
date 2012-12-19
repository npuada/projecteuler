#define MAX 15
#include <stdio.h>
#include <stdlib.h>

int main() {
	int a[MAX][MAX]={{75,0,0,0,0,0,0,0,0,0,0,0,0,0,0},{95,64,0,0,0,0,0,0,0,0,0,0,0,0,0},{17,47,82,0,0,0,0,0,0,0,0,0,0,0,0},{18,35,87,10,0,0,0,0,0,0,0,0,0,0,0},{20,4,82,47,65,0,0,0,0,0,0,0,0,0,0},{19,01,23,75,03,34,0,0,0,0,0,0,0,0,0},{88,02,77,73,07,63,67,0,0,0,0,0,0,0,0},{99,65,4,28,06,16,70,92,0,0,0,0,0,0,0},{41,41,26,56,83,40,80,70,33,0,0,0,0,0,0},{41,48,72,33,47,32,37,16,94,29,0,0,0,0,0},{53,71,44,65,25,43,91,52,97,51,14,0,0,0,0},{70,11,33,28,77,73,17,78,39,68,17,57,0,0,0},{91,71,52,38,17,14,91,43,58,50,27,29,48,0,0},{63,66,4,68,89,53,67,30,73,16,69,87,40,31,0},{4,62,98,27,23,9,70,98,73,93,38,53,60,04,23}};

	int sum[MAX][MAX] = {0};
	int i, j, max;
	sum[0][0] = a[0][0];
	for(i=1; i < MAX; i++) {
		for(j = 0; j <= i; j++) {
			if(j == 0)
				max = sum[i-1][0];
			else if(j == i)
				max = sum[i-1][j-1];
			else
				max = sum[i-1][j-1] > sum[i-1][j] ? sum[i-1][j-1] : sum[i-1][j];
			sum[i][j] = a[i][j] + max;
			printf("%04d ", sum[i][j]);
		}
		printf("\n");
	}
	
	for(i=0; i<MAX; i++)
		printf("%d ", sum[MAX-1][i]);
	return 0;
}