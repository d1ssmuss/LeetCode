class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Follow up: Could you find an O(n + m) solution?
        print([i for i in grid])
        return sum([1 for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] < 0])


print(Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))