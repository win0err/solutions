#include <stdio.h>

int main()
{
	unsigned int t;
	unsigned long n;

	scanf("%d", &t);

	while (t--) {
		scanf("%ld", &n);
		printf("%lu\n", (n + 1) / 2);
	}

	return 0;
}
