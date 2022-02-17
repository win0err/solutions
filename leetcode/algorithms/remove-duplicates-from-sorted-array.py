from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_uniq_idx = 0
        for idx in range(1, len(nums)):
            if nums[last_uniq_idx] != nums[idx]:
                last_uniq_idx += 1
                nums[last_uniq_idx] = nums[idx]

        return last_uniq_idx + 1
