class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        result = []
        i = 0
        
        # for loop for iteration on every element
        for i in range(n-2):
            if(i > 0 and nums[i]== nums[i-1]):
                continue
            left = i+1
            right = n - 1
            total = -1 * nums[i]
            while(left < right):
                Sum = nums[left] + nums[right]
                if  Sum == total:
                    result.append([nums[i],nums[left],nums[right]])
                    left +=1
                    right-=1
                    while ( left < n and nums[left] == nums[left-1]):
                        left+=1
                    while ( right >= 0 and nums[right] == nums[right+1]):
                        right -=1
                elif Sum < total :
                    left+=1
                else :
                    right-=1    
        return result
            



        
        

        