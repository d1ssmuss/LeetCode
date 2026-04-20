class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        mx = -1
        for i in range(len(colors)):
            for j in range(i, len(colors)):
                if colors[i] != colors[j]:
                    mx = max(mx, abs(i-j))
        return mx
