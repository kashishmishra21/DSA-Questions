class Solution(object):
    def backspaceCompare(self, s, t):
        i = len(s) - 1
        j = len(t) - 1


        skip_s = 0
        skip_t = 0

        while i >= 0 or j >= 0:

        # Find the next valid character in s
            while i >= 0:
                if s[i] == '#':
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break

        
            while j >= 0:
                if t[j] == '#':
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break

        # If one string has no valid character left
            if i < 0 or j < 0:
                return i == j

        # Compare valid characters
            if s[i] != t[j]:
                return False

        # Move both pointers left
            i -= 1
            j -= 1

        return True
