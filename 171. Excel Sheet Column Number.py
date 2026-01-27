import string

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        s = 0
        letters = {string.ascii_uppercase[i]:i+1 for i in range(26)}
        for i in range(len(columnTitle)):
            s += letters[columnTitle[::-1][i]] * (26 ** i)
        return s
        
