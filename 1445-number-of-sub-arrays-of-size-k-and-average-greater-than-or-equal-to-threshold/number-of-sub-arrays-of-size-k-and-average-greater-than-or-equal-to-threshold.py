class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        i = 0  
        j = k -1
        win_sum = sum(arr[:k])
        win_avg = win_sum / k  # avg nikal gya
        count = 0
        if win_avg >= threshold:
            count +=1
        for j in range(k,len(arr)):
            # find sum 
            win_sum -= arr[i]
            win_sum += arr[j]

            i+=1
            win_avg = win_sum / k

            # check 
            if win_avg >= threshold:
                count+=1

        return count
