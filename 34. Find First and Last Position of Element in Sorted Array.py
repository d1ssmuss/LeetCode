class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first_pos, last_pos = -1, -1
        for i in range(len(nums)):
            if nums[i] == target:
                first_pos = i
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                last_pos = i
        return sorted([first_pos, last_pos])
