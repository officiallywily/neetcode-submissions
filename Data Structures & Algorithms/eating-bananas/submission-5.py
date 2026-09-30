class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return -1
        
        largest_pile = 0
        for pile in piles:
            largest_pile = max(largest_pile, pile)

        low = 0
        high = largest_pile
        last_valid = largest_pile
        while low <= high and last_valid:
            hours = 0
            test_rate = (low + high) // 2
            print("low: " + str(low))
            print("high: " + str(high))
            for pile in piles:
                hours += pile // (test_rate or 1)
                if pile % (test_rate or 1) != 0:
                    hours += 1

            if hours > h:
                low = test_rate + 1
            else:
                print("hours: ", hours)
                print("valid condition found: ", test_rate)
                last_valid = min(test_rate, last_valid)
                high = test_rate - 1
        
        return last_valid or 1
                
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