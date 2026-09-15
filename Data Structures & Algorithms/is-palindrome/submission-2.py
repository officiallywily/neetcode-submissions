class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = len(s) - 1
        i = 0
        while i < j and i < len(s) and j > -1:
            if not s[i].isalnum() :
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            print (s[i] + ' ' + s[j])
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1

        return True
