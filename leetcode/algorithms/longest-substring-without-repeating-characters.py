class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = {}
        max_length = 0
        start_pos = -1
        for pos, char in enumerate(s):
            if char in found and start_pos <= found[char]:
                start_pos = found[char]
            else:
                max_length = max(max_length, pos - start_pos)
                
            found[char] = pos
        
        return max_length