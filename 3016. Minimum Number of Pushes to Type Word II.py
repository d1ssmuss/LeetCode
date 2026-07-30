from collections import Counter
import math

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Самые часто повторяющиеся буквы должны быть на 1-ом нажатии
        letters = Counter(word)
        letters = sorted(word, key=lambda x: letters[x], reverse=True)
        count = 0
        word = ''
        for i in letters:
            if i not in word:
                word += i
        full_word = ''.join(letters)
        d = {int(i):[] for i in "1234"}
        for i in range(len(word)):
            d[math.ceil((i + 1) / 8)].append(word[i])
            count += math.ceil((i + 1) / 8) * full_word.count(word[i])
        return count


print(Solution().minimumPushes('abcde'))
print(Solution().minimumPushes('xyzxyzxyzxyz'))
print(Solution().minimumPushes('aabbccddeeffgghhiiiiii'))
# print(Solution().minimumPushes('abcdefggggghiiiiiii'))