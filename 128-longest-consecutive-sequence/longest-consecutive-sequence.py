class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        max_count = 0
        count = 1
        number = set(nums)
       
        for x in number:
            if x-1  not in number:
                while x+1 in number:
                    count+=1
                    x+=1
                max_count = max(max_count,count)
                count = 1
        return max_count


        