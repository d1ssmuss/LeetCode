class Solution:
    def countCommas(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            n = abs(n)
            count = 0
            k = 1
            while (10 ** (3 * k)) <= n:
                count += (min(n, 10 ** (3 * (k + 1)) - 1) - (10 ** (3 * k)) + 1) * k
                k += 1
            return count


# while (num := int(input())):
#     print(Solution().countCommas(num))
