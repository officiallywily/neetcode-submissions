class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        letters: dict[str, int] = {}
        longest = 0
        l = 0

        for r in range(len(s)):
            if s[r] in letters and letters[s[r]] >= l:
                l = letters[s[r]] + 1
            letters[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest


