class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = s[0]
        lt = ''
        for i in s[1:]:
            if i in a:
                lt += i
            a += i
        for j in lt:
            a = a.replace(j, '')
        return s.index(a[0]) if a else -1
