class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        arr = set(nums[0])
        for i in range(1, len(nums)):
            arr = arr & set(nums[i])
        return sorted(list(arr))
