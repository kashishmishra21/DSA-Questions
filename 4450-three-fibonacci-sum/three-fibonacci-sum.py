class Solution(object):
    def threeFibonacciSum(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a , b , c = 0 , 1 , 1
        while a + b + c <= n:

            if a + b + c == n :
                return True

            a, b , c = b , c , b+c
        return False