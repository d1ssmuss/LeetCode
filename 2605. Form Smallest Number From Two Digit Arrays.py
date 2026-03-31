class Solution(object):
    def minNumber(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # общий минимум
        mn = set(nums1) & set(nums2)
        if mn:
            return min(mn)
        else:
            if min(nums1) > min(nums2):
                return int(str(min(nums2)) + str(min(nums1)))
            else:
                return int(str(min(nums1)) + str(min(nums2)))
