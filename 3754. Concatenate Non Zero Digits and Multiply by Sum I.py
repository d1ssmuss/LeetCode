class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            s = sum([int(i) for i in str(n) if i != '0'])
        return int(''.join([i for i in str(n) if i != '0'])) * s


print(Solution().sumAndMultiply(0))