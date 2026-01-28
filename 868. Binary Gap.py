class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = bin(n)[2:]
        a = [i for i in range(len(str(num))) if num[i] == '1']
        a = [a[i+1] - a[i] for i in range(len(a) - 1)]
        return max(a) if a else 0



a = Solution().binaryGap(8)
print(a)