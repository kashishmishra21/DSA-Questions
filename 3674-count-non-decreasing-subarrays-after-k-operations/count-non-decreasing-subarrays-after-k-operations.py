class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Prefix sum
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        # Next greater element
        nxt = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                nxt[i] = stack[-1]

            stack.append(i)

        # Binary lifting
        LOG = n.bit_length()

        jump = [[n] * n for _ in range(LOG)]
        cost = [[0] * n for _ in range(LOG)]

        for i in range(n):
            jump[0][i] = nxt[i]
            j = nxt[i]

            cost[0][i] = (
                nums[i] * (j - i) - (pref[j] - pref[i])
            )

        for p in range(1, LOG):
            for i in range(n):
                mid = jump[p - 1][i]

                if mid < n:
                    jump[p][i] = jump[p - 1][mid]
                    cost[p][i] = (
                        cost[p - 1][i] + cost[p - 1][mid]
                    )
                else:
                    cost[p][i] = cost[p - 1][i]

        # Calculate operations for subarray [l, r]
        def getCost(l, r):
            total = 0
            pos = l

            for p in range(LOG - 1, -1, -1):
                if jump[p][pos] <= r:
                    total += cost[p][pos]
                    pos = jump[p][pos]

            total += (
                nums[pos] * (r - pos + 1)
                - (pref[r + 1] - pref[pos])
            )

            return total

        # Sliding window
        ans = 0
        left = 0

        for right in range(n):
            while left <= right and getCost(left, right) > k:
                left += 1

            ans += right - left + 1

        return ans