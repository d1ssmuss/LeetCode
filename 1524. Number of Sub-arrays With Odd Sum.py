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
