class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in seen:
                continue
            counter = 1
            while (num + 1) in seen:
                counter += 1
                num += 1
            longest = max(longest, counter)
        return longest