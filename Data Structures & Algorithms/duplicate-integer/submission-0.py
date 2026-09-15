class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute force method:
        #   iterate through the integer array and for each integer,
        #   iterate through the integer array until you reach an 
        #   identical integer
        #   If there is a repeat, return true,
        #   if the entire array is exhausted, return false
        # Time: O(n^2)
        # Space: O(n)

        # Optimal solution:
        # create a set and add elements as we iterate through the integer
        # array.
        # True if the element exists in the set
        # False if the entire array is exhausted without finding a 
        # match in the set
        # Time: O(n)
        # Space: O(n), higher than brute force method

        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False