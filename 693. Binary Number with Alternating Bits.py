class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = bin(n)[2:]
        for i in range(len(n) - 1):
            if not (n[i] != n[i + 1]):
                return False
        else:
            return True
        
