class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # // har jgh two pointers nhi lgana hota hai
        min_price = prices[0]
        max_price = 0
        for i in range(len(prices)):
            
            min_price = min(min_price,prices[i])
            profit = prices[i] - min_price
            max_price = max(max_price, profit)
        return max_price
