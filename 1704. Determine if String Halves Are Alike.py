class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        first = s[:len(s) // 2]
        second = s[len(s) // 2:]
        count_1 = sum([1 for i in first if i in 'aeiou'])
        count_2 = sum([1 for i in second if i in 'aeiou'])
        return count_1 == count_2
