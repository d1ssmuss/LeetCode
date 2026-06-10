class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in range(len(nums)):
            n = sum(list([int(i) for i in str(nums[num])]))
            if n == num:
                return num
        return -1
