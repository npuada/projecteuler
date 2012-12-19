#include <stdio.h>

int main() {
	int i, j;

	long long sum = 0LL, n = 1LL, x = 1e10;
	for(i = 1; i < 1000; i++) {
		n = i;		
		for(j = 1; j < i; j++) {
			n *= i;
			n %= x;
		}

		sum += n;
	}

	printf("%lld", sum%x);

	return 0;
}
