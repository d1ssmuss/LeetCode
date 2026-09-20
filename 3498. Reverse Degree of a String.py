class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        # print(123 - ord('a'))
        # print(123 - ord('z'))
        sm = 0
        n = len(s)
        for i in range(n):
            sm += (i + 1) * (123 - ord(s[i]))
        return sm
