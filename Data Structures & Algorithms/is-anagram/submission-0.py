class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_counts = {}
        for letter in s:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
        for letter in t:
            if letter not in letter_counts:
                return False
            if letter_counts.get(letter) == 0:
                return False
            letter_counts[letter] -= 1

        for value in letter_counts.values():
            if value != 0:
                return False
        
        return True