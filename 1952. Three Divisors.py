class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
                print(i)
            if count > 3:
                return False
        return True if count == 3 else False
