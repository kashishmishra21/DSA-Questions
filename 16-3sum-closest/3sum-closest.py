class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        i = 0
        for i in range(n-2):
            left = i+1
            right = n-1
            while( left < right):
                current_sum = nums[i] + nums[left] + nums[right] # current sum show krega
                # check the closest
                if(abs(current_sum - target) < abs(closest - target)):
                    closest = current_sum
                if (current_sum < target):
                    left +=1
                else:
                    right-=1
        return closest

            

        
        