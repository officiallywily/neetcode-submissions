class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table: set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in table:
                curr_num = num
                curr_streak = 1
                while (curr_num + 1) in table:
                    curr_num += 1
                    curr_streak += 1

                longest = max(longest, curr_streak)
        
        return longest


        

        