#include <stdio.h>

void kadane_max_subarray(int *array, size_t size,
			 int *best_low, int *best_high, int *best_sum)
{
	int sum = -1;

	int low;
	for (size_t i = 0; i < size; i++) {
		if (sum <= 0) {
			low = i;
			sum = array[i];
		} else {
			sum += array[i];
		}

		if (sum > *best_sum) {
			*best_sum = sum;
			*best_low = low;
			*best_high = i + 1;
		}
	}

	return;
}

void main(void)
{
	int a[] = { 13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7 };	// 18, 20, -7, 12 : 43

	int min = -1, max = -1, sum = 0;

	kadane_max_subarray(a, sizeof(a) / sizeof(a[0]), &min, &max, &sum);

	printf("(");
	for (int i = min; i < max; ++i) {
		printf("%d%s", a[i], i != max - 1 ? ", " : "");
	}
	printf(") %d\n", max);
}
