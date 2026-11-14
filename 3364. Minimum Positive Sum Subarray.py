class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = 10 ** 6 # должна быть > 0
        for r_0 in range(l, r + 1):
            for i in range(len(nums) - r_0 + 1):
                # print(nums[i:i + r_0])
                if sum(nums[i:i + r_0]) > 0:
                    min_sum = min(min_sum, sum(nums[i:i + r_0]))
        return min_sum if min_sum != 10 ** 6 else -1
