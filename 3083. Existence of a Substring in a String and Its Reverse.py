class Solution:
    def isSubstringPresent(self, s) -> bool:
        reverse_s = s[::-1]
        for i in range(len(s) - 1):
            word = s[i:i+2]
            if word in reverse_s:
                return True
        return False


print(Solution().isSubstringPresent('leetcode'))
print(Solution().isSubstringPresent('abcba'))
print(Solution().isSubstringPresent('abcd'))