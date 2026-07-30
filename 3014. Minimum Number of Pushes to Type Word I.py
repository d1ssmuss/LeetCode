from collections import Counter
import math


class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Самые часто повторяющиеся буквы должны быть на 1-ом нажатии
        letters = Counter(word)
        letters = sorted(word, key=lambda x: letters[x], reverse=True)
        count = 0
        word = ''
        for i in letters:
            if i not in word:
                word += i
        # full_word = ''.join(letters)
        for i in range(len(word)):
            # print(f"{i} / 8 = {math.ceil(i / 8)}")
            count += math.ceil((i + 1) / 8)
        return count



print(Solution().minimumPushes('abcde'))
print(Solution().minimumPushes('xycdefghij'))
print(Solution().minimumPushes('abcdefghiiiiiii'))
# print(Solution().minimumPushes('abcdefggggghiiiiiii'))