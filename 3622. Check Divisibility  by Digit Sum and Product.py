class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 9:
            return False
        num = n
        s, p = 0, 1
        while n != 0:
            last = n % 10
            s += last
            p *= last
            n //= 10
        return True if num % (s + p) == 0 else False