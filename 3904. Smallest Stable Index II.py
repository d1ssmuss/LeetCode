class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mn = []
        mx = []

        max_value = nums[0]
        for i in range(0, n):
            if nums[i] >= max_value:
                max_value = nums[i]
            mx.append(max_value)

        min_value = float('inf')
        for i in range(n - 1, -1, -1):
            if nums[i] < min_value:
                min_value = nums[i]
            mn.append(min_value)

        for j in range(len(mx)): # можно и mn
            if (mx[j] - mn[n - j - 1]) <= k:
                return j
        else:
            return -1
