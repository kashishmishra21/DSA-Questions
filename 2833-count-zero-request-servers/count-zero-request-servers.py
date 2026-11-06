from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        logs.sort(key=lambda a: a[1])

        q = sorted([(q, i) for i, q in enumerate(queries)])

        count = defaultdict(int)
        ans = [0] * len(queries)

        left = right = 0
        active = 0

        for time, idx in q:

            while right < len(logs) and logs[right][1] <= time:
                server = logs[right][0]

                if count[server] == 0:
                    active += 1

                count[server] += 1
                right += 1

            while left < right and logs[left][1] < time - x:
                server = logs[left][0]

                count[server] -= 1

                if count[server] == 0:
                    active -= 1

                left += 1

            ans[idx] = n - active

        return ans