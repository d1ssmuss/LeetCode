class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            if '0' in str(n):
                return n
            else:
                mul = 1
                for i in range(len(str(n))):
                    mul *= int(str(n)[i])
                if mul % t == 0:
                    return n
                else:
                    n += 1
