class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        for i in nums:
            if i not in stack:
                stack.append(i)
            else:
                return i