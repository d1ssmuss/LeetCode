class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        new_grid = [[grid[j][i] for i in range(n)] for j in range(m)]
        count = 0
        while count != k:
            for i in range(m):
                for j in range(n):
                    if j == n - 1:
                        # print(i, j, '!', (i + 1) % m, 0)
                        new_grid[(i + 1) % m][0] = grid[i][j]
                    else:
                        # print(i, j)
                        new_grid[i][j + 1] = grid[i][j]
            count += 1
            grid = [[new_grid[j][i] for i in range(n)] for j in range(m)]
            # print(grid, new_grid)
        return new_grid


print(Solution().shiftGrid([[1,2,3],[4,5,6],[7,8,9]], k = 1))
print(Solution().shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))
print(Solution().shiftGrid([[100]], k = 4))
print(Solution().shiftGrid([[1,2,3],[4,5,6],[7,8,9]], k = 9))
print(Solution().shiftGrid([[1, 2, 3, 4],[5, 6, 7, 8]], k = 1))