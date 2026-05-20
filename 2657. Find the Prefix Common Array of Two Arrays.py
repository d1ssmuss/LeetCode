class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        c = []
        for i in range(len(A)):
            c.append(len(set(A[:i + 1]) & set(B[:i + 1])))
        return c
