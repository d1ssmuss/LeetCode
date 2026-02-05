class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            res.append(nums[(nums[i] + i) % len(nums)])
        return res

print(Solution().constructTransformedArray([3,-2,1,1]))
print(Solution().constructTransformedArray([-1,4,-1]))