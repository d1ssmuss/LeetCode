class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        s = [a]
        if b > 0:
            for j in range(1, b + 1):
                s.append(1)
        elif b < 0:
            for j in range(b, 0):
                s.append(-1)
        return sum(s)
