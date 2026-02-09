class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(map(int, s))
        num = ''
        while len(num) != 2:
            num = ''
            for i in range(len(s) - 1):
                num += str((s[i] + s[i + 1]) % 10)
            s = list(map(int, num))
        return True if num[0] == num[1] else False




print(Solution().hasSameDigits("3902"))
print(Solution().hasSameDigits("34789"))