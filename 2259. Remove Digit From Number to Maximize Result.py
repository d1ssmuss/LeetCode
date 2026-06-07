class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        Вам дается строковый номер, представляющий собой целое положительное число, и символьная цифра.

        Верните результирующую строку после удаления ровно одного вхождения цифры из number таким образом, чтобы значение результирующей строки в десятичной форме было максимальным. Тестовые примеры генерируются таким образом, чтобы цифра встречалась в number хотя бы один раз.
        """
        mx = -1
        for i in range(len(number)):
            if number[i] == digit:
                num = number[:i] + number[i+1:]
                mx = max(mx, int(num))
        return mx

print(Solution().removeDigit('123', '3'))
print(Solution().removeDigit('1231', '1'))
print(Solution().removeDigit('551', '5'))
print(Solution().removeDigit('133235', '3'))
