#!/usr/bin/env python3
from typing import List


def merge_sort(A: List) -> List:
    """Merge sort algorithm"""
    if len(A) > 1:
        mid = len(A) // 2

        L, R = A[:mid], A[mid:]
        n1, n2 = len(L), len(R)

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            A[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            A[k] = R[j]
            j += 1
            k += 1

    return A


if __name__ == "__main__":
    ints = [-2, 99, 0, -743, 2, 3, 4]
    merge_sort(ints)

    print(ints)
