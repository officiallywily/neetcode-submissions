class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        window_count = [0] * 26

        # Initialize first window
        orda = ord('a')
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - orda] += 1
            window_count[ord(s2[i]) - orda] += 1
        
        # Calculate initial matches
        matches = 0
        for i in range(26):
            if s1_count[i] == window_count[i]:
                matches += 1
        
        # Slide the fixed window across the rest of s2
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: 
                return True

            # Add the new character on the right
            index_r = ord(s2[r]) - orda
            window_count[index_r] += 1
            
            # if the addition fixes a mismatch
            if window_count[index_r] == s1_count[index_r]:
                matches += 1
            # if the addition breaks a perfect match
            elif window_count[index_r] == s1_count[index_r] + 1:
                matches -= 1
            
            index_l = ord(s2[l]) - orda
            window_count[index_l] -= 1

            # if the removal fixes a mismatch
            if window_count[index_l] == s1_count[index_l]:
                matches += 1
            # if the removal breaks a perfect match
            elif window_count[index_l] == s1_count[index_l] - 1:
                matches -= 1
            
            l += 1
        
        return matches == 26

            