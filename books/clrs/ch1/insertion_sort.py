#!/usr/bin/env python3
import operator
from typing import List

def insertion_sort(a: List, compare=operator.gt) -> List:
    """Insertion sort algorithm"""
    for j in range(1, len(a)):
        key = a[j]

        i = j - 1
        while i >= 0 and compare(a[i], key):
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key

    return a

if __name__ == "__main__":
    ints = [-2, 99, 0, -743, 2, 3, 4]

    print(
        insertion_sort(ints),
        insertion_sort(ints, operator.lt),
        sep='\n'
    )