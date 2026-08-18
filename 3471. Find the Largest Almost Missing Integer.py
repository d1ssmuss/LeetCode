class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        d = {num:0 for num in set(nums)}
        for i in range(len(nums) - k + 1):
            print(nums[i:i + k])
            for j in set(nums[i:i+k]):
                d[j] += 1
        arr = [k for k,v in d.items() if v == 1]
        if len(arr) == 0:
            return -1
        else:
            return max(arr)
