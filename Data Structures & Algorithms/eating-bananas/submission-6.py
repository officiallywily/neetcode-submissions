class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return -1
        
        largest_pile = max(piles)

        low = 1
        high = largest_pile
        last_valid = largest_pile
        while low <= high and last_valid:
            hours = 0
            test_rate = (low + high) // 2
            for pile in piles:
                hours += math.ceil(pile / test_rate)

            if hours > h:
                low = test_rate + 1
            else:
                last_valid = min(test_rate, last_valid)
                high = test_rate - 1
        
        return last_valid
                
# piles=[312884470]
# h=968709470
# hours         = 2 + 1 + 1 + 1 = 5 > 4
# low           = 25
# high          = 25
# test_rate     = 24
# last_valid    = 
# expected: 25

# Binary search for the minimum amount of bananas per hour
# Keep track of the last valid bananas per hour each iteration
# Keep going until low >= high
# 