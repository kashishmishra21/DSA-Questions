from math import gcd

class Solution:
    def maxLength(self, nums):
        n = len(nums)
        ans = 2

        for i in range(n):
            for j in range(i + 1, n):

                valid = True

                for k in range(i, j):
                    if gcd(nums[k], nums[j]) != 1:
                        valid = False
                        break

                if not valid:
                    break

                ans = max(ans, j - i + 1)

        return ans