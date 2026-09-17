class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge cases        
        if t == "" or len(t) > len(s):
            return ""
        
        # keep count of characters in t
        t_count: Dict[str, int] = {}
        window_count: Dict[str, int] = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1


        # 'have' tracks how many unique characters in 't' currently meet the requirements
        # 'need' is the total number of unique characters required
        have, need = 0, len(t_count)

        #store the best result as [left_index, right_index] and its length
        res, res_len = [-1, -1], float("infinity")
        l = 0
        
        for r in range(len(s)):
            char = s[r]
            window_count[char] = 1 + window_count.get(char, 0)

            # If the current character is in 't' and we just reached the exact count needed
            if char in t_count and window_count[char] == t_count[char]:
                have += 1
            
            # Once the window is valid, try to shrink it from the left
            while have == need:
                # Update our minimum window if the current one is smaller
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                # Pop the leftmost character out of the window
                left_char = s[l]
                window_count[left_char] -= 1

                # If popping that character makes our window invalid, decrement 'have'
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    have -= 1
                
                # Move the left pointer forward
                l += 1

        left, right = res
        return s[left: right + 1] if res_len != float("infinity") else ""