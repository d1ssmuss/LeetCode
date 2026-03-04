class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr.sort()
        d = [(i, bin(i)[2:].count('1')) for i in arr]
        d = sorted(d, key=lambda item: item[1])
        return [i[0] for i in d]

print(Solution().sortByBits([0,1,2,3,4,5,6,7,8]))
print(Solution().sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))
print(Solution().sortByBits([1000, 1000]))
