#include <stdio.h>

void merge(int *A, int p, int q, int r)
{
	int n1 = q - p + 1;
	int n2 = r - q;

	int L[n1], R[n2];

	for (int i = 0; i < n1; i++)
		L[i] = A[p + i];

	for (int j = 0; j < n2; j++)
		R[j] = A[q + j + 1];

	int i = 0, j = 0, k = p;

	while (i < n1 && j < n2) {
		if (L[i] < R[j]) {
			A[k] = L[i];
			i++;
		} else {
			A[k] = R[j];
			j++;
		}

		k++;
	}

	while (i < n1) {
		A[k] = L[i];
		i++;
		k++;
	}

	while (j < n2) {
		A[k] = R[j];
		j++;
		k++;
	}
}

void merge_sort(int *array, int p, int r)
{
	if (p < r) {
		int q = (p + r) / 2;

		merge_sort(array, p, q);
		merge_sort(array, q + 1, r);

		merge(array, p, q, r);
	}
}

int main(void)
{
	int ints[] = { -2, 99, 0, -743, 2, 3, 4 };
	int size = sizeof(ints) / sizeof(ints[0]);

	merge_sort(ints, 0, size - 1);

	for (int i = 0; i < size; i++)
		printf("%d ", ints[i]);

	printf("\n");

	return 0;
}
