class Solution:
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        ans = float('inf')

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        for i in range(n):
            for j in range(l, r + 1):
                if i + j <= n:
                    total = prefix[i + j] - prefix[i]

                    if total > 0:
                        ans = min(ans, total)

        return ans if ans != float('inf') else -1