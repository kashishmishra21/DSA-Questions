class Solution(object):
    def totalFruit(self, fruits):

        """
        :type fruits: List[int]
        :rtype: int
        """
        
        left = 0
        right = 0
        hash = {}
        max_len = 0
       # add numbers in hashmap 
        for right in range(len(fruits)):
            if fruits[right] not in hash:
                hash[fruits[right]] = 1
            else :
                hash[fruits[right]] +=1
        # shrink if number is exceed
            while len(hash) > 2 :
                hash[fruits[left]] -=1
                if hash[fruits[left]] == 0:
                    del hash[fruits[left]]
                left +=1
            if len(hash) <= 2:
                lenght = right - left + 1
                max_len = max(max_len,lenght)
            
        return max_len
        



        