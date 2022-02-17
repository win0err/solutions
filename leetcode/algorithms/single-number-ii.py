from collections import defaultdict


class Solution:
    def hashmap(self, nums: List[int]) -> int:
        uniq = defaultdict(int)

        for n in nums:
            uniq[n] += 1

        for i in uniq:
            if uniq[i] != 3:
                return i
