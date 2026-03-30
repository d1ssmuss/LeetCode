class Solution(object):
    def minNumber(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        minimum1 = min(nums1)
        minimum2 = min(nums2)
        a = [i for i in nums1 if i in nums2]
        if a == []:
            return min(int(str(minimum1) + str(minimum2)), int(str(minimum2) + str(minimum1)))
        else:
            return min(a)
