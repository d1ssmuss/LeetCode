class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n % 2 != 0:
            if n == 1:
                return s
            else:
                a = sorted(s[:n // 2])
                return ''.join(a) + s[n // 2] + ''.join(a[::-1])
        else:
            a = sorted(s[:n // 2])
            return ''.join(a) + ''.join(a[::-1])

print(Solution().smallestPalindrome('z'))
print(Solution().smallestPalindrome('babab'))
print(Solution().smallestPalindrome('daccad'))
print(Solution().smallestPalindrome('aayxxyaa'))