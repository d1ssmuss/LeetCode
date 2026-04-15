class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        letters = {'b': 0, 'a':0, 'l_1':0, 'l_2':0, 'o_1':0, 'o_2':0, 'n':0}
        for letter in text:
            if letter in 'ban':
                letters[letter] += 1
            elif letter == 'l':
                if letters['l_1'] != letters['l_2']:
                    letters['l_2'] += 1
                else:
                    letters['l_1'] += 1
            elif letter == 'o':
                if letters['o_1'] != letters['o_2']:
                    letters['o_2'] += 1
                else:
                    letters['o_1'] += 1
        return min(letters.values())
        убираем лишние чёрные буквы
        len(answ) / len(set(answ))
