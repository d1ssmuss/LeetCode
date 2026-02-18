import math

class Solution(object):
    def vowelConsonantScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        Вам предоставляется строка s, состоящая из строчных английских букв, пробелов и цифр.

        Пусть v - количество гласных в s, а c - количество согласных в s.
        
        Гласная - это одна из букв "a", "e", "i", "o" или "u", в то время как любая другая буква в английском алфавите считается согласной.
        
        Оценка строки s определяется следующим образом:
        
        Если c > 0, оценка = floor(v / c), где floor обозначает округление в меньшую сторону до ближайшего целого числа.
        В противном случае оценка = 0.
        Возвращает целое число, обозначающее оценку строки.
        """
        vowel = 0
        consonant = 0
        for i in s:
            if i.isalpha():
                if i in 'aeiou':
                    vowel += 1
                else:
                    consonant += 1
        if consonant > 0:
            return math.floor(vowel / consonant)
        else:
            return 0




print(Solution().vowelConsonantScore('cooear'), 2)
print(Solution().vowelConsonantScore('axeyizou'), 1)
print(Solution().vowelConsonantScore('au 123'), 0)
