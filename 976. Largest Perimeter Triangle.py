from itertools import combinations


class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = 0
        s = tuple(sorted(list(combinations(nums, 3))))
        for i in s:
            if i[0] < i[1] + i[2] and i[2] < i[0] + i[1] and i[1] < i[0] + i[2]:
                if i[0] + i[1] + i[2] > mx:
                    mx = i[0] + i[1] + i[2]
        return mx if mx != 0 else 0


print(Solution().largestPerimeter([2,1,2]))
print(Solution().largestPerimeter([1,2,1,10]))
print(Solution().largestPerimeter([3,2,3,4]))