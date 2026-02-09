class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k not in nums:
            return k
        else:
            n = k
            while n in set(nums):
                n += k
        return n


print(Solution().missingMultiple(nums = [8,2,3,4,6], k = 2))
print(Solution().missingMultiple(nums = [1,4,7,10,15], k = 5))
print(Solution().missingMultiple([8,2,3,4,6], 2))