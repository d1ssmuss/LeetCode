class Solution:
    def minOperations(self, s: str) -> int:
        nums_1 = [int(i) for i in s]
        nums_2 = [int(i) for i in s]
        count_1 = 0
        count_2 = 0
        for i in range(len(nums_1) - 1):
            if nums_1[i] == nums_1[i + 1]:
                if nums_1[i] == 0:
                    nums_1[i + 1] = 1
                else:
                    nums_1[i + 1] = 0
                count_1 += 1
        if nums_2[0] == 1:
            nums_2[0] = 0
        else:
            nums_2[0] = 1
        count_2 += 1
        for i in range(len(nums_2) - 1):
            if nums_2[i] == nums_2[i + 1]:
                if nums_2[i] == 0:
                    nums_2[i + 1] = 1
                else:
                    nums_2[i + 1] = 0
                count_2 += 1
        return min(count_1, count_2)
        # return nums, count

print(Solution().minOperations("1111")) # 2
print(Solution().minOperations("10")) # 0
print(Solution().minOperations("0100")) # 1
print(Solution().minOperations("110010")) # 2
print(Solution().minOperations("10010100")) # 3