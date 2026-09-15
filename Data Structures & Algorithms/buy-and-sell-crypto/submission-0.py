class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = highest = prices[0]
        max_profit = 0
        for price in prices:
            if price < lowest:
                lowest = highest = price
            if price > highest:
                highest = price
                max_profit = max(highest - lowest, max_profit)

        return max_profit