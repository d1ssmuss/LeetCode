class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [0, 1, 1]
        for i in range(2, n):
            arr.append(arr[-1] + arr[-2] + arr[-3])
        return arr[n]
