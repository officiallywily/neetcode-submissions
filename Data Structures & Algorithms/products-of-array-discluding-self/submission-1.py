class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret_arr = [1] * len(nums)

        left_prod = 1
        for i in range(len(nums)):
            ret_arr[i] = left_prod
            left_prod *= nums[i]
        
        right_prod = 1
        for i in reversed(range(len(nums))):
            ret_arr[i] *= right_prod
            right_prod *= nums[i]
        
        return ret_arr
        