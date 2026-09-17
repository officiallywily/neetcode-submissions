class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_letters: Dict[str, int] = {}
        for char in s1: 
            target_letters[char] = target_letters.get(char, 0) + 1
        
        l = 0
        window_letters: Dict[str, int] = {}
        for r, char in enumerate(s2):
            window_letters[char] = window_letters.get(char, 0) + 1
            if r - l + 1 == len(s1):
                for letter in target_letters:
                    if target_letters == window_letters:
                        return True
                
                window_letters[s2[l]] -= 1
                if window_letters[s2[l]] == 0:
                    del window_letters[s2[l]]
                l += 1


        return False