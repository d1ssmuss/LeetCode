class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = set(s)
        d = {i:s.count(i) for i in letters}
        d_sort = sorted(d.items(), key=lambda item: item[1])
        answ = ''
        for k, v in d_sort:
            answ += k * v
        return answ[::-1]
