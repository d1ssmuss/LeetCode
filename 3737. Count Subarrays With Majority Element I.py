class Solution:
    def countMajoritySubarrays(self, nums, target):
        count = 0
        for i in range(len(nums)):
            count_target = 0
            for j in range(i, len(nums)):
                if nums[j] == target:
                    count_target += 1
                if count_target > (j - i + 1) / 2: # > 50 %
                    count += 1
        return count



print(Solution().countMajoritySubarrays(nums = [1,2,2,3], target = 2))
print(Solution().countMajoritySubarrays(nums = [1,1,1,1], target = 1))
print(Solution().countMajoritySubarrays(nums = [1,2,3], target = 4))