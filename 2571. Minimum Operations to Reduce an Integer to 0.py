import math

class Solution:
    def minOperations(self, n: int) -> int:
        k = 1
        while (n & (n - 1)) != 0:
            p = int(math.log2(n))
            n = min(n - 2 ** p, 2 ** (p + 1) - n)
            k += 1
        return k



print(Solution().minOperations(39)) # 3
print(Solution().minOperations(54)) # 3
print(Solution().minOperations(79)) # 3
print(Solution().minOperations(16)) # 1
