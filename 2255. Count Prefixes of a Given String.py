class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        count = 0
        for word in words:
            if s[:len(word)] == word:
                count += 1
        return count


print(Solution().countPrefixes(words = ["a","b","c","ab","bc","abc"], s = "abc"))
print(Solution().countPrefixes(words = ["a","a"], s = "aa"))