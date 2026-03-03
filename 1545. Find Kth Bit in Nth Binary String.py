class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = ['0']
        for i in range(n):
            num = nums[-1] + '1' + (bin((int(nums[-1], 2) ^ 2 ** len(nums[-1]) - 1))[2:])[::-1]
            nums.append(num)
        return nums[-1][k - 1]
