class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_avg = float(window_sum) / k
        i = 0


        for j in range(k, len(nums)):
            window_sum -= nums[i]
            window_sum += nums[j]
            i += 1

            current_avg = float(window_sum) / k
            max_avg = max(max_avg, current_avg)

        print("Final window_sum:", window_sum)
        print("Final max_avg:", max_avg)
        print("Test average:", 51 / 4)

        return max_avg

