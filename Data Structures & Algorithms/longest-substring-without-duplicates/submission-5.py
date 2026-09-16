class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        longest = 0
        for r, letter in enumerate(s):
            if letter in seen and seen[letter] >= l:
                l = seen[letter] + 1
            seen[letter] = r
            longest = max(longest, r - l + 1)
        return longest