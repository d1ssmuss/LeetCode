class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        mx = 0
        k = 0
        for i in range(len(s)):
            if s[i] == '(':
                k += 1
            elif s[i] == ')':
                k -= 1
            mx = max(mx, k)
        return mx
                
