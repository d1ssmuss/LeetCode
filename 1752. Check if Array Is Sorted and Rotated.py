class Solution:
    def check(self, nums):
        # nums = [nums[-1]] + nums[:len(nums)-1]
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            nums = [nums[-1]] + nums[:len(nums) - 1]
            # print(i, nums)
            if nums == sorted_nums:
                return True
        else:
            return False

print(Solution().check([3,4,5,1,2]))
print(Solution().check([2,1,3,4]))
print(Solution().check([1,2,3]))