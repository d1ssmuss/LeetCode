class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        s = word
        d = {i:[] for i in set(s.lower())}
        count = 0
        for letter in s:
            d[letter.lower()].append(letter)
        # print(d)
        for v in d.values():
            # print(v[0])
            letter = v[0][0].lower()
            shablon = letter + letter.upper()
            # print(''.join(v))
            if letter in v and letter.upper() in v and shablon in "".join(v) and shablon[::-1] not in ''.join(v):
                count += 1
        return count
