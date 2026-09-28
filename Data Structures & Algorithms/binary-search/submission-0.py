class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        low = 0
        high = len(nums) - 1
        mid = high // 2

        while nums[mid] != target and low < high:
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            mid = (high + low) // 2
            
        if nums[mid] == target: 
            return mid
        return -1

        # nums=[-1,0,2,4,6,8]
        # target=4
        # low = 3
        # mid = 2 => 2
        # high = 5