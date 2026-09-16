class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize an array for 128 ASCII characters with -1 
        # (-1 means "we haven't seen this character yet")
        seen = [-1] * 128
        
        l = 0
        longest = 0
        
        for r in range(len(s)):
            # ord() gets the ASCII integer value of the character (e.g., 'a' -> 97)
            char_code = ord(s[r])
            
            # Check if the character's last seen index is within our window
            if seen[char_code] >= l:
                l = seen[char_code] + 1
                
            # Overwrite the array slot with the new index
            seen[char_code] = r
            
            # Calculate the window size
            longest = max(longest, r - l + 1)
            
        return longest