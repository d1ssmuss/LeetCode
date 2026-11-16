class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        """
        н + н = ч
        н + ч = ч + н = н
        ч + ч =
        :param arr:
        :return:
        """
        even, odd, res = 0, 0, 0
        for x in arr:
            if x % 2 == 0:
                even += 1
            else:
                even, odd = odd, even + 1
            res += odd
        return res % (10 ** 9 + 7)


print(Solution().numOfSubarrays([1, 3, 5])) # 4
print(Solution().numOfSubarrays([2, 4, 6])) # 0
print(Solution().numOfSubarrays([1, 2, 3, 4, 5, 6, 7])) # 16
print(Solution().numOfSubarrays([1, 3, 5, 9, 10])) # 8
print(Solution().numOfSubarrays([1, 2, 5, 9, 10])) # 8
print(Solution().numOfSubarrays([2, 4, 5, 6])) # 6
