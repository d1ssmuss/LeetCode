class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for num in nums:
            for digit in str(num):
                arr.append(int(digit))
        return arr
