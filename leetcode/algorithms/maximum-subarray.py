from math import inf
from typing import List
from abc import ABC, abstractmethod


class Solution(ABC):
    @abstractmethod
    def maxSubArray(self, nums: List[int]) -> int:
        pass


class Kadane(Solution):
    def maxSubArray(self, nums: List[int]) -> int:
        sum = best_sum = -inf

        for num in nums:
            sum = max(num, sum + num)
            best_sum = max(best_sum, sum)

        return best_sum


class DivideAndConquer(Solution):
    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSumSubarray(nums, 0, len(nums) - 1)

    @classmethod
    def maxCrossingSubarray(cls, nums: List[int], low: int, mid: int, high: int) -> int:
        left_sum = -inf
        sum = 0

        for i in range(mid, low - 1, -1):
            sum += nums[i]
            left_sum = max(sum, left_sum)

        right_sum = -inf
        sum = 0

        for i in range(mid + 1, high + 1):
            sum += nums[i]
            right_sum = max(sum, right_sum)

        return left_sum + right_sum

    @classmethod
    def maxSumSubarray(cls, nums: List[int], low: int, high: int) -> int:
        if low == high:
            return nums[high]

        mid = (low + high) // 2

        left_sum = cls.maxSumSubarray(nums, low, mid)
        right_sum = cls.maxSumSubarray(nums, mid + 1, high)
        crossing_sum = cls.maxCrossingSubarray(nums, low, mid, high)

        return max(left_sum, right_sum, crossing_sum)
