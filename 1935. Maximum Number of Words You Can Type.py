class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        count = 0
        for word in text.split():
            # print(set(word), )
            if len(set(word) & set(brokenLetters)) == 0:
                count += 1
        return count


print('bc' in ['a', 'b', 'c'])
print(Solution().canBeTypedWords(text = "hello world", brokenLetters = "ad")) # 1
print(Solution().canBeTypedWords(text = "leet code", brokenLetters = "lt")) # 1
print(Solution().canBeTypedWords(text = "leet code", brokenLetters = "e")) # 0