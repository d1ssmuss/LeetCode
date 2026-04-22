class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        answ = []
        for word in queries:
            for word_dict in dictionary:
                if sum([1 for i in range(len(word)) if word[i] != word_dict[i]]) <= 2:
                    answ.append(word)
                    break
        return answ
