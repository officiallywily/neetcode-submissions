class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        prefix_mult = 1
        suffix_mult = 1
        for i in range(len(nums)):
            prefix[i] = prefix_mult
            suffix[len(nums) - 1 - i] = suffix_mult
            prefix_mult *= nums[i]
            suffix_mult *= nums[len(nums) - 1 - i]
        
        ret = []
        for i in range(len(nums)):
            ret.append(prefix[i] * suffix[i])
        
        return ret