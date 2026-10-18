class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack  = []
        for ch in s :
            if len(stack) == 0 :
                stack.append(ch)
                pass
            elif ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)