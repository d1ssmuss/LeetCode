class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count_one = 0
        count_more = 0
        for i in nums:
            if i >= 10:
                count_more += i
            else:
                count_one += i
        return True if count_one != count_more else False
