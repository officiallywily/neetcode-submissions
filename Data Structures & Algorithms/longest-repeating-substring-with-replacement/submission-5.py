class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts: Dict[str, int] = {}
        l = 0
        longest = 0
        max_f = 0

        for r, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            max_f = max(max_f, counts[char])
            while (r - l + 1 - max_f) > k:
                counts[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        
        return longest
        
                