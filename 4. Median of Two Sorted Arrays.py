import math

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        if (len(nums1) + len(nums2)) % 2 == 0:
            # Вернуть float с 5 знаками после запятой
            return round((nums[int(len(nums) / 2) - 1] + nums[int(len(nums) / 2)]) / 2, 5)
        else:
            return round(nums[math.ceil(len(nums) / 2) - 1], 5)

print(Solution().findMedianSortedArrays([1,2],[3,4]))
print(Solution().findMedianSortedArrays([0,0,0,0,0], [-1,0,0,0,0,0,1]))
print(Solution().findMedianSortedArrays([1,3],[2]))
# print(math.ceil(9/2))