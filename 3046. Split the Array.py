class Solution:
    def isPossibleToSplit(self, nums):
        nums.sort()
        nums1 = []
        nums2 = []
        for i in nums:
            if i not in nums1 and len(nums1) == len(nums2):
                nums1.append(i)
            else:
                nums2.append(i)
        return True if len(set(nums1)) == len(nums1) & len(set(nums2)) == len(nums2) else False



print(Solution().isPossibleToSplit([1,1,2,2,3,4]))
print(Solution().isPossibleToSplit([1,1,1,1]))
print(Solution().isPossibleToSplit([8,9,8,5,9,3,3,1,2,1]))