class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_s = list(s)
        indexes = []
        letters = []
        for i in range(len(s)):
            if s[i].lower() in 'aeiou':
                letters.append(s[i])
                indexes.append(i)
        # print(indexes, letters)
        for j in range(len(indexes) // 2):
            # print(j, len(indexes) - j - 1, indexes[j], indexes[len(indexes) - j - 1])
            list_s[indexes[j]] = letters[len(indexes) - j - 1]
            list_s[indexes[len(indexes) - j - 1]] = letters[j]
        return ''.join(list_s)
