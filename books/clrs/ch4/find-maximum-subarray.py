#!/usr/bin/env python3
from typing import List
from math import inf


class CLRSSolution:
    def __init__(self, A: List):
        self.A = A

    def _findMaxCrossingSubarray(
        self, low: int, mid: int, high: int
    ) -> (int, int, int):
        max_left = max_right = None

        left_sum = -inf
        sum = 0
        for i in range(mid - 1, low - 1, -1):
            sum += A[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i

        right_sum = -inf
        sum = 0
        for i in range(mid, high):
            sum += A[i]
            if sum > right_sum:
                right_sum = sum
                max_right = i

        return max_left, max_right + 1, left_sum + right_sum

    def _findMaxSubarray(self, low: int, high: int) -> (int, int, int):
        if low >= high - 1:
            return (low, high, self.A[low])
        else:
            mid = (low + high) // 2

            left_low, left_high, left_sum = self._findMaxSubarray(low, mid)
            right_low, right_high, right_sum = self._findMaxSubarray(mid, high)
            cross_low, cross_high, cross_sum = self._findMaxCrossingSubarray(
                low, mid, high
            )

            if left_sum >= right_sum and left_sum >= cross_sum:
                return left_low, left_high, left_sum
            elif right_sum >= left_sum and right_sum >= cross_sum:
                return right_low, right_high, right_sum
            else:
                return cross_low, cross_high, cross_sum

    def find(self) -> List:
        low, high, _ = self._findMaxSubarray(0, len(self.A))

        return self.A[low:high]

    def findSum(self) -> int:
        _, _, sum = self._findMaxSubarray(0, len(self.A))

        return sum


class KadaneSolution:
    def __init__(self, A: List):
        self.A = A

    def _findMaxSubarray(self, low: int, high: int) -> (int, int, int):
        best_low = best_high = None
        best_sum = sum = -inf

        for i in range(low, high):
            if sum <= 0:
                low = i
                sum = self.A[i]
            else:
                sum += self.A[i]

            if sum > best_sum:
                best_sum = sum
                best_low = low
                best_high = i + 1

        return best_low, best_high, best_sum

    def find(self) -> List:
        low, high, _ = self._findMaxSubarray(0, len(self.A))

        return self.A[low:high]

    def findSum(self) -> int:
        best_sum = -inf
        sum = 0

        for i in self.A:
            sum = max(i, sum + i)
            best_sum = max(best_sum, sum)

        return best_sum


if __name__ == "__main__":
    A = (13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7)

    clrs = CLRSSolution(A)
    kadane = KadaneSolution(A)

    print(clrs.find(), clrs.findSum())
    print(kadane.find(), kadane.findSum())
