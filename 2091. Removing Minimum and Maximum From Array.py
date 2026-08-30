class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mn, mx = nums[0], nums[0]
        n = len(nums)
        mn_index, mx_index = 0,0
        for i in range(len(nums)):
            if nums[i] < mn:
                mn = nums[i]
                mn_index = i
            elif nums[i] > mx:
                mx = nums[i]
                mx_index = i
        mn_index += 1
        mx_index += 1
        if mn == mx:
            return 1
        else:
            # print(f'1-ый индекс {mn_index}')
            # print(f'2-ый индекс {mx_index}')
            # print(f'n - 1-ый индекс {n - mn_index}')
            # print(f'n - 2-ый индекс {n - mx_index}')
            first, second = min(mn_index, mx_index), max(mn_index, mx_index)
            a = first + (second - first)
            b = first + (n - second + 1)
            # c = (n - second + 1) + (n - first + second + 1)
            c = n - min(mn_index, mx_index) + 1
            print(a, b, c)
            return min(a,b,c)


print(Solution().minimumDeletions(nums = [1, 2, 4, 3, -1]))
print(Solution().minimumDeletions(nums = [100, 2, 4, 3, -1]))
print(Solution().minimumDeletions(nums = [2,10,7,5,4,1,8,6]))
print(Solution().minimumDeletions(nums = [0,-4,19,1,8,-2,-3,5]))
print(Solution().minimumDeletions(nums = [101]))
print(Solution().minimumDeletions(nums = [-1,-53,93,-42,37,94,97,82,46,42,-99,56,-76,-66,-67,-13,10,66,85,-28]))
print(Solution().minimumDeletions(nums = [-14,61,29,-18,59,13,-67,-16,55,-57,7,74]))
