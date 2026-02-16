class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        # return sorted(target) == sorted(arr)
        # return {i:target.count(i) for i in set(target)} == {i:arr.count(i) for i in set(arr)}
        a = {i:0 for i in set(target)}
        b = {i: 0 for i in set(arr)}
        for i in target:
            a[i] += 1
        for i in arr:
            b[i] += 1
        return a == b

"""
True
True
False
"""
print(Solution().canBeEqual(target = [1,2,3,4], arr = [2,4,1,3]))
print(Solution().canBeEqual(target = [7], arr = [7]))
print(Solution().canBeEqual(target = [3,7,9], arr = [3,7,11]))
print(Solution().canBeEqual(target = [1,2,2,3], arr = [1,1,2,3]))

