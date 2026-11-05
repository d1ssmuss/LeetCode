class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        distance = 0
        arr2 = list(set(arr2))
        n, m = len(arr1), len(arr2)
        for i in range(n):
            flag = False
            for j in range(m):
                if abs(arr1[i] - arr2[j]) <= d:
                    flag = True
            if flag == False:
                distance += 1
        return distance
