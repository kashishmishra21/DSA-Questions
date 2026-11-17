class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0
                    groups = length // d

                    for offset in range(d):
                        left = i + offset
                        right = i + offset + (groups - 1) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[i][j] = min(cost[i][j], changes)

    

        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for g in range(1, k + 1):
            for end in range(2 * g, n + 1):
                for start in range(2 * (g - 1), end - 1):

                    dp[g][end] = min(
                        dp[g][end],
                        dp[g - 1][start] + cost[start][end - 1]
                    )

        return dp[k][n]