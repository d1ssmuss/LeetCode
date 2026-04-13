class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        # print(nums[start:])
        indexes = [i for i in range(len(nums)) if nums[i] == target]
        mn = float('+inf')
        for j in indexes:
            mn = min(mn, abs(j - start))
        return mn
