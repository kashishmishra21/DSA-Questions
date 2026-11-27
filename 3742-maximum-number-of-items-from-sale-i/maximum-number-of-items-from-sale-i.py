from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        free = [0] * n

        # Count free items for each item type
        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free[i] += 1

        min_price = min(item[1] for item in items)

        # 0/1 Knapsack
        dp = [0] * (budget + 1)

        for i in range(n):
            price = items[i][1]
            value = 1 + free[i]

            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + value)

        ans = 0

        for b in range(budget + 1):
            extra = (budget - b) // min_price
            ans = max(ans, dp[b] + extra)

        return ans