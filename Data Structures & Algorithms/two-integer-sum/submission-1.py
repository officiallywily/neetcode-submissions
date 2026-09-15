class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in targets:
                return [targets[diff], i]

            targets[num] = i
        return [0, 0]
        