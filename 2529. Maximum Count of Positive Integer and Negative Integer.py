class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = []
        neg = []
        for i in nums:
            if i > 0:
                pos.append(i)
            elif i < 0:
                neg.append(i)
        return max(len(pos), len(neg))
