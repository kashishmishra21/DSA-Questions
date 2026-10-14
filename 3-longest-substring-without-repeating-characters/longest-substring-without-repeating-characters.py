class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = 0
        hash = {}
        max_len = 0
        for r in range(len(s)):
            
            if s[r] not in hash:
                hash[s[r]] = 1
            else:
                hash[s[r]] +=1
        # shrink  kr dega jb tak duplicate hai
            while hash[s[r]] > 1:
                hash[s[l]] -=1
                if hash[s[l]] == 0:
                    del hash[s[l]]
                l +=1
            lenght = r - l + 1
            max_len = max(max_len,lenght)
        return max_len
            
            

        