class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        # count = 0
        # for i in list(set(words1) & set(words2)):
        #     if words1.count(i) == 1 and words2.count(i) == 1:
        #         count += 1
        # return count
        
        # count = 0
        # w_1 = {word:words1.count(word) for word in set(words1)}
        # w_2 = {word:words2.count(word) for word in set(words2)}
        # return len(set([k for k,v in w_1.items() if v == 1]) & set([k for k,v in w_2.items() if v == 1]))

        d = {word:0 for word in set(words1) & set(words2)}
        for word in words1 + words2:
            try: # ???
                d[word] += 1
            except:
                pass
        return len([word for k,v in d.items() if v == 2])
