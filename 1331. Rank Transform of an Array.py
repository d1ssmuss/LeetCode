class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        array = sorted(set(arr))
        d = {array[i]:i+1 for i in range(len(array))}
        # print(array, d)
        return [d[i] for i in arr]
        # sorted_arr = sorted(set(arr))
        # d = {j:i for i,j in enumerate(sorted_arr, start=1)}
        # return [d[i] for i in arr]
