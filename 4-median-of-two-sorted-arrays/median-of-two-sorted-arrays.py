class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # djdbwecbewjcbhjc
        
        s_arr = sorted(nums1 + nums2)
        len_arr = len(s_arr)
        if len_arr % 2 != 0 :
            mid = len_arr // 2
            return s_arr[mid]
        else:
            left = (len_arr // 2) -1
            right = len_arr // 2
            median =  (s_arr[left] + s_arr[right]) / 2.0
            return median

        