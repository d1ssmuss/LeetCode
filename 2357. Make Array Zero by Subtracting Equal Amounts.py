class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        d = set(nums)
        if 0 in d:
            d.remove(0)
        k = 0
        while sum(d) != 0:
            mn = min(d)
            d = {i - mn for i in d}
            d.remove(0)
            k += 1
        return k
