#include <stdio.h>

int main() {
	int i;

	long long j = 1LL, x = 1e10;
	for(i = 1; i <= 7830457; i++) {
		j *= 2;
		j %= x;
	}

	j *= 28433;
	j++;
	printf("%lld", j%x);

	return 0;
}
