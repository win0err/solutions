from math import inf
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''Kadane's algorithm'''
        sum = best_sum = -inf

        for num in nums:
            sum = max(num, sum + num)
            best_sum = max(best_sum, sum)

        return best_sum
