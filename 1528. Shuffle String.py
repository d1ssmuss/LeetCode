class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        d = {indices[i]:s[i] for i in range(len(indices))}
        return ''.join(d.values())
