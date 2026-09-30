class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]: # the left side is sorted
                if nums[l] <= target < nums[mid]: # the target is in the left block
                    r = mid - 1
                else:
                    l = mid + 1
            else: # the right side is sorted
                if nums[mid] < target <= nums[r]: # the target is in right block
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1