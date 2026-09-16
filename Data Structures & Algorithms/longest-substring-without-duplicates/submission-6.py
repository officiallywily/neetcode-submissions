class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = [-1] * 128
        longest = 0

        for r, letter in enumerate(s):
            if seen[ord(letter)] >= l:
                l = seen[ord(letter)] + 1
            seen[ord(letter)] = r
            longest = max(longest, r - l + 1)
        return longest