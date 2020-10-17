#!/usr/bin/env python3
from typing import List
from math import inf

class CLRSSolution:
    def __init__(self, A: List):
        self.A = A
        
    def _findMaxCrossingSubarray(self, low: int, mid: int, high: int):
        max_left = max_right = None

        left_sum = -inf
        temp_sum = 0
        for i in range(mid, low-1, -1):
            temp_sum += A[i]
            if temp_sum > left_sum:
                left_sum = temp_sum
                max_left = i

        right_sum = -inf
        temp_sum = 0
        for i in range(mid+1, high+1):
            temp_sum += A[i]
            if temp_sum > right_sum:
                right_sum = temp_sum
                max_right = i
        
        return (max_left, max_right, left_sum+right_sum)

    def _findMaxSubarray(self, low, high):
        if high == low: 
            return (low, high, self.A[low])
        else:
            mid = (low + high) // 2

            left_low, left_high, left_sum = self._findMaxSubarray(low, mid)
            right_low, right_high, right_sum = self._findMaxSubarray(mid + 1, high)
            cross_low, cross_high, cross_sum = self._findMaxCrossingSubarray(low, mid, high)

            if left_sum >= right_sum and left_sum >= cross_sum:
                return left_low, left_high, left_sum
            elif right_sum >= left_sum and right_sum >= cross_sum:
                return right_low, right_high, right_sum
            else:
                return cross_low, cross_high, cross_sum

    def find(self) -> List:
        low, high, _ = self._findMaxSubarray(0, len(self.A) - 1)

        return self.A[low:high + 1]
    
    def findSum(self) -> int:
        _, _, sum = self._findMaxSubarray(0, len(self.A) - 1)

        return sum

class KadaneSolution:
    def __init__(self, A: List):
        self.A = A

    def find(self) -> List:
        best_start = best_end = None
        current_start = current_end = None
        best_sum = current_sum = -inf

        for current_end, x in enumerate(self.A):
            if current_sum <= 0:
                current_start = current_end
                current_sum = x
            else:
                current_sum += x

            if current_sum > best_sum:
                best_sum = current_sum
                best_start = current_start
                best_end = current_end + 1

        return self.A[best_start:best_end]

    def findSum(self) -> int:
        best_sum = -inf
        current_sum = 0

        for x in self.A:
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)

        return best_sum


if __name__ == "__main__":
    A = (13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7)

    clrs = CLRSSolution(A)
    kadane = KadaneSolution(A)

    print(clrs.find(), clrs.findSum())
    print(kadane.find(), kadane.findSum())