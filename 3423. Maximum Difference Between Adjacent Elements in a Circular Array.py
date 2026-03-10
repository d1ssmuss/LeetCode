class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = []
        for i in range(len(nums)):
            prev = nums[i-1]
            nxt = nums[i]
            t = abs(prev - nxt)
            mx.append(t)
        return max(mx)
