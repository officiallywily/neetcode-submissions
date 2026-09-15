class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret_list = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            target = nums[i] * -1

            while j < k:
                total = nums[j] + nums[k]
                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                elif total == target:
                    ret_list.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while k > j and k < len(nums) - 1 and nums[k] == nums[k + 1]:
                        k -= 1
        
        return ret_list
            

        
