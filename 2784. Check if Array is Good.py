class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = max(nums)
        arr = [i for i in range(1, n)] + [n, n]
        return sorted(arr) == sorted(nums)


print(Solution().isGood([1, 3, 3, 2]))
print(Solution().isGood([1]))