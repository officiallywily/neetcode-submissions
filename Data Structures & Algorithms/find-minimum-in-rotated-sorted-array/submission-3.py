class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]

        l, r = 1, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] < nums[0]: # the target is to the left
                r = mid - 1
            else:
                l = mid + 1
        