class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_op = 0
        s = sum(nums)
        while s % k != 0:
            s -= 1
            min_op += 1
        return min_op
