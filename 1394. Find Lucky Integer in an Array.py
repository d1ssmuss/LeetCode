class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mx = 0
        for i in set(arr):
            if arr.count(i) == i:
                if i > mx:
                    mx = i
        return mx if mx else -1

a = Solution().findLucky(arr = [2,2,2,3,3])
print(a)