class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        cnt = 0
        # arr = []
        for i in range(len(words)):
            for j in range(len(words)):
                if set(words[j]) == set(words[i]) and i != j:
                    cnt += 1
                    # arr.append((i, j))
        return cnt // 2
