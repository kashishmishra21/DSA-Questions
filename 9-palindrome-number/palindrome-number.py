class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = 0
        d = x
        while ( x > 0):
            rev = (rev * 10) + x % 10
            x = x // 10
        if rev == d:
            return True
        else:
            return False

        