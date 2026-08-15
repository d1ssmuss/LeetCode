class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if set(nums) == {0}:
            return 0
        else:
            nums.sort()
            left, right = 0, len(nums) - 1
            mx_len_left, mx_len_right = -1, -1
            while True:
                result = 0
                for i in nums[left:right + 1]:
                    result ^= i
                if result == 0:
                    left += 1
                else:
                    mx_len_left = len(nums[left:right + 1])
                    break
            left = 0
            while True:
                result = 0
                for i in nums[left:right + 1]:
                    result ^= i
                if result == 0:
                    right -= 1
                else:
                    mx_len_right = len(nums[left:right + 1])
                    break
            return max(mx_len_left, mx_len_right)




print(Solution().longestSubsequence([1, 2, 3]))
print(Solution().longestSubsequence([2, 3, 4]))
print(Solution().longestSubsequence([0, 0]))
print(Solution().longestSubsequence([0,0,7,0,0,0,7,0,0]))
# print(0 ^ 0 ^ 7 ^ 0 ^ 0 ^ 0 ^ 7 ^ 0 ^ 0) # 0
print(1 ^ 2 ^ 3)
