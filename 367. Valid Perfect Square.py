class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = num ** 0.5
        if x - int(x) != 0:
            return False
        else:
            return True
