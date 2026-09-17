class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def _findMajority(counts: Dict) -> str:
            most: int = 0
            for letter, count in counts.items():
                if count > most:
                    most: int = count
                    majority: str = letter
            return majority
        
        def _findReplaced(counts: Dict, majority: str) -> int:
            count: int = 0
            for letter, number in counts.items():
                if letter != majority:
                    count += number
            return count
                
        l = 0
        counts: Dict[str, int] = {}
        longest = 0

        for r, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            majority = _findMajority(counts)
            replaced = _findReplaced(counts, majority)
            # print("analyzing char: " + char)
            # print("string section: " + s[l:r + 1])
            # print("counts: " + str(counts))
            # print("majority: " + majority)
            # print("l: " + str(l) + "\tr: " + str(r))
            # print("replaced: " + str(replaced))
            while replaced > k:
                # print("replacing limit reached")
                # print("replaced: " + str(replaced))
                # print("counts: " + str(counts))
                # print("majority: " + majority)
                counts[s[l]] -= 1
                l += 1
                majority = _findMajority(counts)
                replaced = _findReplaced(counts, majority)
            longest = max(longest, r - l + 1)
            # print("")
        
        return longest
        
                