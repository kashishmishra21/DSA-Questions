class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        # Step 1: Build the original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Step 2: Build the modified tree
        new_children = [[] for _ in range(n)]
        last = [-1] * 26
        new_parent = [-1] * n

        stack = [(0, 0, -1)]

        while stack:
            node, state, prev = stack.pop()
            char = ord(s[node]) - ord('a')

            if state == 0:
                # Find the nearest ancestor with the same character
                nearest = last[char]

                if node != 0:
                    if nearest != -1:
                        new_parent[node] = nearest
                    else:
                        new_parent[node] = parent[node]

                    new_children[new_parent[node]].append(node)

                # Update the latest ancestor for this character
                last[char] = node

                # Exit event
                stack.append((node, 1, prev))

                # Visit original children
                for child in reversed(children[node]):
                    stack.append((child, 0, last[ord(s[child]) - ord('a')]))

            else:
                # Restore previous character ancestor
                last[char] = prev

        # Step 3: Calculate subtree sizes in the modified tree
        answer = [1] * n
        order = []
        stack = [0]

        while stack:
            node = stack.pop()
            order.append(node)

            for child in new_children[node]:
                stack.append(child)

        # Process nodes in reverse order
        for node in reversed(order):
            if new_parent[node] != -1:
                answer[new_parent[node]] += answer[node]

        return answer