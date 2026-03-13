class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        while s != '1':
            if s[-1] == '0':
                n = n // 2
            else:
                n += 1
            count += 1
        return count
