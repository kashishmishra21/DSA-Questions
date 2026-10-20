class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0 :
            return 0
        if x == 2 :
            return x-1
        elif x == 1:
            return x
        i = 2
        while i * i <= x:
            i +=1
        return i-1