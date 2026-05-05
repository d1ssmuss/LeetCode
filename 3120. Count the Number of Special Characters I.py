class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        count = 0
        s = []
        for letter in word:
            if letter not in s:
                if letter.islower():
                    if letter.upper() in word:
                        count += 1
                else:
                    if letter.lower() in word:
                        count += 1
            s.append(letter)
        return count // 2
