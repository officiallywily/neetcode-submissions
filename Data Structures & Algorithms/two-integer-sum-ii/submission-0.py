class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i: int = 0
        j: int = len(numbers) - 1

        while i < j:
            the_sum = numbers[i] + numbers[j]
            if the_sum > target:
                j -= 1
            if the_sum < target:
                i += 1
            
            if the_sum == target:
                return [i + 1, j + 1]
        
        return [0, 0] # safe fall back, likely never reaches this line