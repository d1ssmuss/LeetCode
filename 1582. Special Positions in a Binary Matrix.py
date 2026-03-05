class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])

        row_ones = [0] * m
        col_ones = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_ones[i] += 1
                    col_ones[j] += 1
        # print(row_ones, col_ones)

        count = 0
        for i in range(m):
            for j in range(n):
                if row_ones[i] == 1 and col_ones[j] == 1 and mat[i][j] == 1:
                    count += 1
        return count




print(Solution().numSpecial([[1,0,0],[0,0,1],[1,0,0]]))
print(Solution().numSpecial([[1,0,0],[0,1,0],[0,0,1]]))
print(Solution().numSpecial([[0,0],[0,0],[1,0]]))
# print(Solution().numSpecial([[1,2,3],[4,5,6],[7,8,9]]))
"""
1 2 3
4 5 6
7 8 9
"""
print(Solution().numSpecial([[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,1,0,0]]))
# 0 0 1 0
# 0 0 0 0
# 0 0 0 0
# 0 1 0 0