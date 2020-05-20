#include <stdio.h>

void insertion_sort(int* A, size_t l)
{
    for (int j = 1; j < l; j++) {
        int key = A[j];

        int i;
        for (i = j - 1; i >= 0 && A[i] >= key; i--) {
            A[i + 1] = A[i];
        }

        A[i + 1] = key;
    }
}

int main(void)
{
    int ints[] = { -2, 99, 0, -743, 2, 3, 4 };
    int size = sizeof(ints) / sizeof(ints[0]);

    insertion_sort(ints, size);
 
    for (int i = 0; i < size; i++)
        printf("%d ", ints[i]);
 
    printf("\n");
 
    return 0;
}