class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        is_negative = False
        if num < 0:
            num = num * (-1)
            is_negative = True
        elif num == 0:
            return '0'
        s = ''
        while num > 0:
            s += str(num % 7)
            num //= 7
        return s[::-1] if is_negative == False else str('-' + s[::-1])
