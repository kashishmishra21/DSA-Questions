class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        lenght = 0
        low = 0 
        high =0
        n = len(nums)
        result = float("inf") # infinity hai 
        total = 0
        while (high < n):
            total = total + nums[high]
            #firing krni hAI
            while(total >= target):
                lenght = high - low + 1
                result = min(result,lenght)
                total = total - nums[low]
                low +=1

            high+=1
        if result == float("inf"):
            return 0
        return result


            


        