class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def _findMajority(counts: Dict) -> str:
            most: int = 0
            for letter, count in counts.items():
                if count > most:
                    most: int = count
                    majority: str = letter
            return majority
                
        l = 0
        counts: Dict[str, int] = {}
        longest = 0

        for r, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            majority = _findMajority(counts)
            replaced = r - l + 1 - counts[majority]
            while replaced > k:
                counts[s[l]] -= 1
                l += 1
                majority = _findMajority(counts)
                replaced = r - l + 1 - counts[majority]
            longest = max(longest, r - l + 1)
        
        return longest
        
                