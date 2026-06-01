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
        mx = max(nums)
        mn = min(nums)
        c = 0
        for i in nums:
            if i != mx and i != mn:
                c += 1
        return c
