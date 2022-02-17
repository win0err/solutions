from typing import List


class Solution:
    def bits(self, nums: List[int]) -> int:
        missing = len(nums)

        for i, n in enumerate(nums):
            missing ^= i ^ n

        return missing

    def math(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2

        return expected - sum(nums)
