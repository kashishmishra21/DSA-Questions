class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        both = min(need1, need2)

        # Option 1: Buy common items for both requirements
        cost = both * min(costBoth, cost1 + cost2)

        # Remaining requirements
        rem1 = need1 - both
        rem2 = need2 - both

        # Buy remaining items individually or use type 3
        cost += rem1 * min(cost1, costBoth)
        cost += rem2 * min(cost2, costBoth)

        return cost