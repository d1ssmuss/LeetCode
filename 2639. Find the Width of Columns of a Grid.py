class Solution(object):
    def findColumnWidth(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        row, column = len(grid[0]), len(grid)
        d = {i:0 for i in range(row)}
        for i in range(row):
            for j in range(column):
                d[i] = max(d[i], len(str(grid[j][i])))
        return d.values()
