class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack = []
        stack2 = []
        for ch in s:
            if ch != "#":
                stack.append(ch)
            elif stack:
                stack.pop()
        for ch in t:
            if ch != "#":
                stack2.append(ch)
            elif stack2:
                stack2.pop()
        return stack == stack2



        