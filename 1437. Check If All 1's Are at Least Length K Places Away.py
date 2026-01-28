class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        arr = [i for i in range(len(nums)) if nums[i] == 1]
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i+1]) <= k:
                return False
        else:
            return True
