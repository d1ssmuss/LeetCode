class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        left = 0
        right = len(nums) - 1
        while len(arr) != len(nums):
            if abs(nums[left]) < abs(nums[right]):
                arr.append(nums[right] ** 2)
                right -= 1
            else:
                arr.append(nums[left] ** 2)
                left += 1
        return arr[::-1]


"""
[1, 9, 16, 100]
[9, 9, 49, 121]
[4, 9, 1, 25]
"""
print(Solution().sortedSquares([-4,-1,0,3,10]))
print(Solution().sortedSquares([-7,-3,2,3,11]))
print(Solution().sortedSquares([-5,-3,-2,-1]))