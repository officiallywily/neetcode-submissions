class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters: List[int] = [0] * 26
        for i in range(len(s)):
            s_index = ord(s[i]) - ord('a')
            t_index = ord(t[i]) - ord('a')
            letters[s_index] += 1
            letters[t_index] -= 1

        for i in range(26):
            if letters[i] != 0:
                return False

        return True