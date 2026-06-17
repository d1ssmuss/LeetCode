class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {i:0 for i in set(nums)}
        for i in nums:
            d[i] += 1
        return [k for k, v in d.items() if v > len(nums) // 3]
