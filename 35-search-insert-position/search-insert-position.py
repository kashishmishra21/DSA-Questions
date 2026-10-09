class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        count =0
        while i < len(nums):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                i +=1
                count = i
            elif nums[i] > target:
                return i
        return count 
        