class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n ^ int('1' * len(bin(n)[2:]), 2)


print(Solution().bitwiseComplement(10))
print(Solution().bitwiseComplement(5))
print(Solution().bitwiseComplement(2))
print(Solution().bitwiseComplement(7))
print(Solution().bitwiseComplement(0))