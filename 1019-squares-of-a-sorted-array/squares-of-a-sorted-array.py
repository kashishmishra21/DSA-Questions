class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = []
        neg = []
        for num in nums:
            if(num < 0):
                neg.append(num)
            else:
                pos.append(num)
        # case 1 :- No negative number:-
        if(len(neg)==0):
            return [x**2 for x in nums]
        #case 2 :- No positive number
        if(len(pos)==0):
            res = [x**2 for x in nums]
            res.reverse()
            return res
        # case 3 :- Both exists
        i = j = 0
        neg = [x * x for x in neg][::-1]
        pos = [x * x for x in pos]
        n = len(neg)
        m = len(pos)
        result =[]
        while( i < n and j < m):
            if (neg[i] <= pos[j]):
                result.append(neg[i])
                i += 1
            else:
                result.append(pos[j])
                j+=1

        #when your while loop ends
        while( i < n):
         result.append(neg[i])
         i += 1

        while( j < m):
         result.append(pos[j])
         j+=1
        return result

            


        

        