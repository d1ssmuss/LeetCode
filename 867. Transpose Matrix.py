class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        transp = []
        for i in range(len(matrix[0])):
            arr = []
            for j in range(len(matrix)):
                arr.append(matrix[j][i])
            transp.append(arr)
        return transp


print(Solution().transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().transpose([[1,2,3],[4,5,6]]))