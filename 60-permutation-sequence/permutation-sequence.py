import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = list(range(1,n+1))
        fact = math.factorial(n-1)
        k = k - 1
        answer = ""
        while len(numbers) > 0 : 
            
            index = k // fact
            digit = numbers[index]
            answer += str(digit)
            numbers.pop(index)

            k = k - (fact * index)
            if len(numbers) > 0:
                fact = fact // len(numbers)


        return answer





        