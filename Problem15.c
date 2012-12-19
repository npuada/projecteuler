#define MAX 20
#include <stdio.h>

int main() {
	long long x[MAX][MAX] = {0L};
	long long i, j, n;
	for(i = 0; i < MAX; i++) {
		x[0][i] = 1LL;
		x[i][0] = 1LL;
	}

	for(i = 1; i < MAX; i++) {
		for(j = i; j < MAX; j++) {
			long long temp = 0LL;
			x[j][i] = x[i][j] = x[i][j-1] + x[i-1][j];
		}
	}
	
	for(i = 0; i < MAX; i++) {
		for(j = 0; j < MAX; j++) {
			printf("%12lld", x[i][j]);
		}
		printf("\n");
	}

	return 0;
}