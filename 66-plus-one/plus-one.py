class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = 0
        for i in range(len(digits)):
            sum = sum * 10 + digits[i]
        sum +=1
        digits = [int(d) for d in str(sum)]
        return digits


        