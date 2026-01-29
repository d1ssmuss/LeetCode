class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        while nums != sorted(nums):
            min_sum = [nums[i] + nums[i+1] for i in range(len(nums)-1)]
            min_index = min_sum.index(min(min_sum))
            print(min_sum)
            nums = nums[:min_index] + [min_sum[min_index]] + nums[min_index+2:]
            print('>', nums)
            count += 1
        return count

# a = Solution().minimumPairRemoval([5,2,3,1])
# print(a)
# b = Solution().minimumPairRemoval([1,2,2])
# c = Solution().minimumPairRemoval([2,2,-1,3,-2,2,1,1,1,0,-1])
# print(c)
deepseek_test = Solution().minimumPairRemoval([2,-1,-1,3])
print(deepseek_test)

