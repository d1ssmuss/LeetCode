import math

class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        odd, even = [], []
        while len(odd) != n and len(even) != n:
            i = 1
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
            i += 1
        nod = math.gcd(sum(odd), sum(even))
        return nod


print(Solution().gcdOfOddEvenSums(4))
print(Solution().gcdOfOddEvenSums(12))