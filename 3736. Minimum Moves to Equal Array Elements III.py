class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = max(nums)
        count = 0
        for i in range(len(nums)):
            count += mx - nums[i]
        return count
