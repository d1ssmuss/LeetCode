class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nonzeroes = []
        zeroes = []
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            if nums[i] != 0:
                nonzeroes.append(nums[i])
            else:
                zeroes.append(nums[i])
        else:
            if nums[-1] != 0:
                nonzeroes.append(nums[-1])
            else:
                zeroes.append(nums[-1])
        return nonzeroes + zeroes
