class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        k = ''
        mx = 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                k += s[i] + s[i + 1]
            else:
                mx = max(len(k), mx)
                k = ''
        else:
            mx = max(len(k), mx)
        return mx // 2 + 1

print(Solution().maxPower('leetcode'))
print(Solution().maxPower('abbcccddddeeeeedcba'))
print(Solution().maxPower('j'))
print(Solution().maxPower('cc'))
print(Solution().maxPower('ddd'))
print(Solution().maxPower('dddd'))
