class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mn = float('inf')
        index = 0
        for i in range(n):
            if max(nums[:i + 1]) - min(nums[i:]) <= k:
                mn = min(max(nums[:i + 1]) - min(nums[i:]), mn)
                index = i
                break
        return index if mn != float('inf') else -1



print(Solution().firstStableIndex(nums = [5,0,1,4], k = 3))
print(Solution().firstStableIndex(nums = [3, 2, 1], k = 1))
print(Solution().firstStableIndex(nums = [0], k = 0))
print(Solution().firstStableIndex(nums = [0, 0], k = 0))
