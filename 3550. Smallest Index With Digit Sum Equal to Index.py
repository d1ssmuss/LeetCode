# class Solution(object):
#     def smallestIndex(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         for num in range(len(nums)):
#             n = sum(list([int(i) for i in str(nums[num])]))
#             if n == num:
#                 return num
#         return -1
class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            s = 0
            while nums[i] != 0:
                s += nums[i] % 10
                nums[i] //= 10
            if s == i:
                return i
        return -1
