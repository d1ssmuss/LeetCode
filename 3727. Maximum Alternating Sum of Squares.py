class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = [i ** 2 for i in nums]
        # print(nums)
        nums = [i * (-1) if i < 0 else i for i in nums]
        nums.sort()
        print(nums)
        n = len(nums)
        s = 0
        for i in range((n // 2)):
            print(i, s, nums[i], nums[n - 1 - i])
            s += nums[n - i - 1] ** 2 - nums[i] ** 2
        if n % 2 != 0:
            s += nums[n // 2] ** 2
        return s


# print(Solution().maxAlternatingSum([1, 2, 3]))
# print(Solution().maxAlternatingSum([1, -1, 2, -2, 3, -3]))
# print(Solution().maxAlternatingSum([12, -4]))
print(Solution().maxAlternatingSum([-10,-4,15]))
