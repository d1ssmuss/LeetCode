class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {letter:s.count(letter) for letter in set(s)}
        return True if len(set(d.values())) == 1 else False
