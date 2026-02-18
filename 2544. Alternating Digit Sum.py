class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = list(map(int, str(n)))
        s = 0
        for i in range(len(nums)):
            if i % 2 != 0:
                s += -nums[i]
            else:
                s += nums[i]
        return s





print(Solution().alternateDigitSum(521))
print(Solution().alternateDigitSum(111))
print(Solution().alternateDigitSum(886996))