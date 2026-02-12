class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        bank = 0
        count = 0
        day = 1
        monday = 0
        while count != n:
            bank += day + monday
            day += 1
            if day == 8:
                day = 1
                monday += 1
            count += 1
        return bank



print(Solution().totalMoney(4))
print(Solution().totalMoney(10))
print(Solution().totalMoney(20))