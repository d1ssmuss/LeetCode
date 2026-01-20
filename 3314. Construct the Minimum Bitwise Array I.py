class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            if nums[i] <= 2:
                ans.append(-1)
            else:
                for j in range(1, nums[i]):
                    if ((j | (j+1)) == nums[i]):
                        ans.append(j)
                        break
        return ans



# print(10 | 11) # 11 != 2
# print((1 | 2) == 3) # 100
a = Solution().minBitwiseArray(nums=[2,3,5,7])
b = Solution().minBitwiseArray(nums=[11,13,31])
print(a)
print(b)