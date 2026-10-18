class Solution(object):
    def isValid(self, s):
        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
                pass

            else:
                if len(stack) == 0:
                    return False
                if pairs[ch] != stack[-1]:
                    return False
                stack.pop()
              
                pass

        if len(stack) == 0 :
            return True
        else :
            return False
        