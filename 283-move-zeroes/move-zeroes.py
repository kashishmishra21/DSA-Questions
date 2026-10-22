class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0

        if len(nums) <= 1:
            return 
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i +=1
            else:
                continue
        while i < len(nums):
            nums[i] = 0
            i +=1
        

