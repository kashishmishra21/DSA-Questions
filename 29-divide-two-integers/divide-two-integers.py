class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2**31 -1
        INT_MIN = -(2**31)

        if dividend == INT_MIN  and divisor == -1:
            return INT_MAX
        
        if dividend < 0 and divisor < 0 or dividend > 0 and divisor > 0:
            sign = 1
        else:
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)
        quo = 0
        while dividend >= divisor:
            count = 1
            chunk = divisor

            while dividend >= chunk + chunk:
                chunk = chunk + chunk 
                count = count + count
            dividend = dividend - chunk
            quo = quo + count
        if sign == -1:
            return -quo
        else:
            return quo
            

