class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        for i in queries:
            idx = i[0]
            while idx <= i[1]:
                nums[idx] = (nums[idx] * i[3]) % (10 ** 9 + 7)
                idx += i[2]
        x = nums[0]
        for j in nums[1:]:
            x ^= j
        return x



print(Solution().xorAfterQueries(nums = [1,1,1], queries = [[0,2,1,4]])) # 4
print(Solution().xorAfterQueries(nums = [2,3,1,5,4], queries = [[1,4,2,3],[0,2,1,2]])) # 31