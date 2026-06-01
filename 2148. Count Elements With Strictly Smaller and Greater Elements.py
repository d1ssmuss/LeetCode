class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = list(set(nums))
        # sort потом убираем все мин и макс

        # nums.sort()
        # return nums[1:len(nums)-1]

        arr = [i for i in nums if i != min(nums) and i != max(nums)]
        return len(arr)
