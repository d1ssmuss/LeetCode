class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # m - строки
        # n - столбцы
        grid = [['#' for i in range(n)] for j in range(m)]
        print(grid)
        # Координаты последней клетки
        for i in range(m - 1, -1, -1):
            grid[i][n - 1] = '.'
        for j in range(n - 1, -1, -1):
            grid[0][j] = '.'
        return [''.join(i) for i in grid]
