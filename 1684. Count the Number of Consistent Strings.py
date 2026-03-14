class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        return set('abc') <= set('ac')


print(Solution().countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))
print(Solution().countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))
print(Solution().countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]))