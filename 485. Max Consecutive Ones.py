class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        k = 0
        mx = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                k += 1
            else:
                mx = max(mx, k)
                k = 0
        else:
            mx = max(mx, k)
        return mx
