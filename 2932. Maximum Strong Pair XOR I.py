class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = -1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]) and (nums[i] ^ nums[j]) > mx:
                    mx = nums[i] ^ nums[j]
        return mx
