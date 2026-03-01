class Solution(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """
        # arr = list(s)
        # for i in range(len(s), 0, -1):
        #     num = int(''.join(arr[:i]))
        #     if num % 10 == 2:
        #         return num
        # return ''
        if '2' not in s:
            return ''
        else:
            return s[:len(s)-s[::-1].index('2')]

print(Solution().largestEven('1112'))
print(Solution().largestEven('221'))
print(Solution().largestEven('1'))