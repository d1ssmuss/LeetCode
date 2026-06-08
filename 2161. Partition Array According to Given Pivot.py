class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        small = []
        middle = []
        big = []
        for i in nums:
            if i < pivot:
                small.append(i)
            elif i == pivot:
                middle.append(i)
            else:
                big.append(i)
        return small + middle + big
