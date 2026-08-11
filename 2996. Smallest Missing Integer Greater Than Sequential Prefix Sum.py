class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = []
        for i in range(len(nums) - 1):
            n.append(nums[i])
            if nums[i + 1] - nums[i] == 1:
                continue
            else:
                break
        else:
            n.append(nums[-1])
        num = sum(n)
        while True:
            if num in nums:
                num += 1
            else:
                return num
