class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prev_up, prev_down = nums[0], nums[0]
        k = 1
        mx_up, mx_down = 0, 0
        for i in range(n - 1):
            if nums[i + 1] - nums[i] > 0:
                k += 1
            else:
                mx_up = max(mx_up, k)
                k = 1
        else:
            mx_up = max(mx_up, k)
        k = 1
        for i in range(n - 1):
            if nums[i] - nums[i + 1] > 0:
                k += 1
            else:
                mx_down = max(mx_down, k)
                k = 1
        else:
            mx_down = max(mx_down, k)
        return max(mx_down, mx_up)


print(Solution().longestMonotonicSubarray([1,9,7,1]))
print(Solution().longestMonotonicSubarray([1,4,3,3,2]))
