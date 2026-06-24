class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        last = None
        for k in range(0, n + 1):
            a = sum([i for i in range(1, k + 1)])
            b = sum([j for j in range(k, n + 1)])
            if a == b:
                last = k
        return last if last != None else -1
