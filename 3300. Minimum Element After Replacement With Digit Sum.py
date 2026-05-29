class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answ = [sum([int(i) for i in list(str(num))]) for num in nums]
        return min(answ)
