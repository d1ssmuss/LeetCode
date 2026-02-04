class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
                    # print(i,j)
        return count

a = Solution().numIdenticalPairs([1,2,3,1,1,3])
print(a)