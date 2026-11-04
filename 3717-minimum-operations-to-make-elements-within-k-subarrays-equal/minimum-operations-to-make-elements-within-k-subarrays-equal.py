class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums))
        m = len(vals)
        pos = {v: i for i, v in enumerate(vals)}

        class Fenwick:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)

            def add(self, i, val):
                i += 1
                while i <= self.n:
                    self.bit[i] += val
                    i += i & -i

            def query(self, i):
                res = 0
                while i > 0:
                    res += self.bit[i]
                    i -= i & -i
                return res

            def kth(self, k):
                idx = 0
                step = 1 << (self.n.bit_length() - 1)

                while step:
                    nxt = idx + step
                    if nxt <= self.n and self.bit[nxt] < k:
                        idx = nxt
                        k -= self.bit[nxt]
                    step >>= 1

                return idx

        count = Fenwick(m)
        total = Fenwick(m)

        window_sum = 0

        for i in range(x):
            idx = pos[nums[i]]
            count.add(idx, 1)
            total.add(idx, nums[i])
            window_sum += nums[i]

        costs = []

        def get_cost():
            mid = count.kth((x + 1) // 2)
            median = vals[mid]

            lc = count.query(mid)
            ls = total.query(mid)

            rc = x - count.query(mid + 1)
            rs = window_sum - total.query(mid + 1)

            return median * lc - ls + rs - median * rc

        costs.append(get_cost())

        for i in range(x, n):
            old = nums[i - x]
            new = nums[i]

            count.add(pos[old], -1)
            total.add(pos[old], -old)

            count.add(pos[new], 1)
            total.add(pos[new], new)

            window_sum += new - old

            costs.append(get_cost())

        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]