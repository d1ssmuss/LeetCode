class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        primary_diagonal_elements = [mat[i][i] for i in range(len(mat))]
        secondary_diagonal_elements = [mat[i][len(mat) - 1 - i] for i in range(len(mat))]
        if len(mat) % 2 != 0:
            return sum(primary_diagonal_elements) + sum(secondary_diagonal_elements) - mat[len(mat) // 2][len(mat) // 2]
        else:
            return sum(primary_diagonal_elements) + sum(secondary_diagonal_elements)
