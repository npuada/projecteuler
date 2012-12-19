#define MAX 100
#define BUF 1024
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	FILE *in = fopen("triangle.txt", "r");
	int a[MAX][MAX]={0};
	int sum[MAX][MAX] = {0};
	int i, j, max;
	char str[BUF];
	char *tokenPtr;
	
	for(i=0; i<MAX; i++) {
		fgets(str, BUF, in);
		tokenPtr = strtok(str, " ");
		
		j = 0;
		while(tokenPtr != NULL) {
			sscanf(tokenPtr, "%d", &a[i][j]);
			tokenPtr = strtok(NULL, " ");
			j++;
		}
	}	
	
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
		}
	}
	
	max = 0;
	for(i=0; i<MAX; i++)
		if(sum[MAX-1][i] > max)
			max = sum[MAX-1][i];
	printf("%d", max);
	fclose(in);
	return 0;
}