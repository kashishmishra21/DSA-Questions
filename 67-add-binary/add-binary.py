class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        int_a = int(a,2)
        int_b = int(b,2)
        total = int_a + int_b
        result = (bin(total)[2:])

        return result