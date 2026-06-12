class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = [i for i in s if i.isalpha()][::-1]
        new_s = ''
        for i in s:
            if i.isalpha():
                new_s += letters[0]
                letters = letters[1:]
            else:
                new_s += i
        return new_s
