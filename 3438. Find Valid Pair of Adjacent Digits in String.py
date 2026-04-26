class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s) - 1):
            answ = s[i:i+2]
            if s.count(answ[0]) == int(answ[0]) and s.count(answ[1]) == int(answ[1]) and answ[0] != answ[1]:
                return answ
        return ''


print(Solution().findValidPair('2523533'))
print(Solution().findValidPair('1522'))
print(Solution().findValidPair('221'))
print(Solution().findValidPair('22'))