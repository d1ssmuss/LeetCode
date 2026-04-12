class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for word in range(left, right + 1):
            if words[word][0] in vowels and words[word][-1] in vowels:
                count += 1
        return count
