from typing import List


class Solution:
    def bits(self, nums: List[int]) -> int:
        missing = 0

        for n in nums:
            missing ^= n

        return missing

    def math(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
