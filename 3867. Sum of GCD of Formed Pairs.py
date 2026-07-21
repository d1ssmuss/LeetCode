import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixgcd = []
        mx = -1
        s = 0
        for i in range(len(nums)):
            mx = max(mx, nums[i])
            prefixgcd.append(math.gcd(mx, nums[i]))
        prefixgcd.sort()
        middle = len(prefixgcd) // 2 if len(prefixgcd) % 2 != 0 else -1
        # return middle, prefixgcd
        left, right = 0, len(prefixgcd) - 1
        while left != len(prefixgcd) // 2:
            s += math.gcd(prefixgcd[left], prefixgcd[right])
            left += 1
            right -= 1
        return s
