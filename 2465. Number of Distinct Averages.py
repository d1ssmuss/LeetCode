class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        average = []
        while nums != []:
            mn = min(nums)
            mx = max(nums)
            average.append((mn + mx) / 2)
            # print((mn + mx) / 2)
            nums.remove(mn)
            nums.remove(mx)
        return len(set(average))
