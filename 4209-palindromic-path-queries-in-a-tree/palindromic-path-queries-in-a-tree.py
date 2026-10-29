class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        from collections import defaultdict

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = n.bit_length()
        parent = [[-1] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        # Iterative DFS: Euler entry/exit times and parents
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1

                parent[0][u] = p

                stack.append((u, p, 1))

                for v in reversed(adj[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer
                timer += 1

        # Binary lifting table
        for k in range(1, LOG):
            for u in range(n):
                p = parent[k - 1][u]
                if p != -1:
                    parent[k][u] = parent[k - 1][p]

        def is_ancestor(u, v):
            return tin[u] <= tin[v] and tout[v] <= tout[u]

        def lca(u, v):
            if is_ancestor(u, v):
                return u
            if is_ancestor(v, u):
                return v

            for k in range(LOG - 1, -1, -1):
                p = parent[k][u]
                if p != -1 and not is_ancestor(p, v):
                    u = p

            return parent[0][u]

        # Fenwick tree for XOR
        bit = [0] * (2 * n + 2)

        def update_bit(i, val):
            i += 1
            while i < len(bit):
                bit[i] ^= val
                i += i & -i

        def prefix(i):
            res = 0
            i += 1
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        # Each node contributes its character mask at tin[node].
        # The subtree range XOR can be maintained using entry/exit events.
        masks = [1 << (ord(c) - ord('a')) for c in s]

        for u in range(n):
            update_bit(tin[u], masks[u])
            update_bit(tout[u], masks[u])

        def root_path_mask(u):
            # XOR of character masks on the root-to-u path
            return prefix(tin[u])

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                new_mask = 1 << (ord(c) - ord('a'))
                delta = masks[u] ^ new_mask

                update_bit(tin[u], delta)
                update_bit(tout[u], delta)

                masks[u] = new_mask

            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)

                # Root-path XORs include the LCA in both paths.
                # XOR cancels it, so add its character back.
                path_mask = (
                    root_path_mask(u)
                    ^ root_path_mask(v)
                    ^ masks[w]
                )

                # True if at most one bit is set.
                ans.append((path_mask & (path_mask - 1)) == 0)

        return ans