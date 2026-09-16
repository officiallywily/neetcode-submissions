class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        letters: set[str] = set()
        longest = 0
        l = 0
        r = 0
        while l < len(s):
            while r < len(s) and s[r] not in letters:
                letters.add(s[r])
                r += 1
            longest = max(longest, r - l)
            letters.remove(s[l])
            l += 1

        return longest


