class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        if 1 not in arr:
            arr[0] = 1
        for i in range(len(arr)-1):
            if abs(arr[i] - arr[i + 1]) > 1:
                arr[i + 1] = arr[i] + 1
        return arr[-1]
