import math
from functools import reduce
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        mx = -1
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                # print(nums[i:j + 1])
                _gcd = reduce(gcd, nums[i:j + 1])
                prod = reduce(lambda x, y: x * y, nums[i:j + 1])
                _lcm = reduce(lcm, nums[i:j + 1])
                if prod == _lcm * _gcd:
                    # print(nums[i:j + 1], prod, _gcd, _lcm)
                    mx = max(mx, len(nums[i:j + 1]))
        return mx
