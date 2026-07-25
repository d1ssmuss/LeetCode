class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [int(i) for i in str(n)]
        nums.sort()
        return nums[-1] * nums[-2]
