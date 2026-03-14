class Solution(object):
    def countMonobit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        else:
            count = 1
            i = 1
            while (2 ** i) - 1 <= n:
                count += 1
                i += 1
            return count



print(Solution().countMonobit(100))
print(Solution().countMonobit(1))
print(Solution().countMonobit(4))