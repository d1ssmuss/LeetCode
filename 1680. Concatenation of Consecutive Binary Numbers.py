class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = ''
        for i in range(n + 1):
            ans += bin(i)[2:]
        num = int(ans, 2)
        return num % (10 ** 9 + 7)
        
