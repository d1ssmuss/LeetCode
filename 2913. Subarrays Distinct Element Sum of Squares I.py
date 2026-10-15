class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = 0
        for i in range(n):
            for j in range (i, n):
                # print(nums[i:j + 1])
                s += len(set(nums[i:j+1])) ** 2
        return s
                
