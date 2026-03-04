import math


class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return int(bin(n)[2:].replace('0', '1'), 2)
        return (2 ** (int(math.log2(n)) + 1)) - 1



print(Solution().smallestNumber(5))
print(Solution().smallestNumber(10))
print(Solution().smallestNumber(3))