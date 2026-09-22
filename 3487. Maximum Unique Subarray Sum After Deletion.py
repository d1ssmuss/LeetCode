class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Удалять предыдущий если он уже был (или мб отрицательный)
        # Максимум по положительным числам и минимум по отрицательным числам
        # s = set()
        # for i in nums:
        #     if (i not in s):
        #         s.add(i)
        positive_nums = set()
        for i in nums:
            if i not in positive_nums and i >= 0:
                positive_nums.add(i)
        return sum(positive_nums) if positive_nums != set() else max(nums)
            
