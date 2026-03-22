import numpy as np

class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        np_mat = np.array(mat)
        for i in range(1, 4):
            if np.array_equal(np.rot90(np_mat, k=i), target):
                return True
        return False
        

print(Solution().findRotation(mat = [[0,1],[1,0]], target = [[1,0],[0,1]]))
print(Solution().findRotation(mat = [[0,0],[1,0]], target = [[1,0],[0,0]]))
