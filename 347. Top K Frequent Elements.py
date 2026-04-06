class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for i in set(nums):
            d[i] = nums.count(i)
        d = sorted(d.items(), key=lambda item: item[1])
        print(d)
        ans = [d[i][0] for i in range(len(d) - 1, len(d) - k - 1, -1)]
        return ans


print(Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(Solution().topKFrequent(nums = [1], k = 1))
print(Solution().topKFrequent(nums = [1,2,1,2,1,2,3,1,3,2], k = 2))