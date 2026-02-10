class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        if all([True if int(i) % 2 == 0 else False for i in set(num)]):
            return ''
        else:
            for i in range(len(num)):
                if int(num[::-1][i]) % 2 != 0:
                    return num[:len(num) - i]
            else:
                return ''



print(Solution().largestOddNumber('52'))
print(Solution().largestOddNumber('4206'))
print(Solution().largestOddNumber('35427'))