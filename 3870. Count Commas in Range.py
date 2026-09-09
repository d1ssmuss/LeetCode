class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        k = 1
        while True:
            if (10 ** (3 * k)) > n:
                break
            else:
                count += (min(n, 10 ** (3 * (k + 1)) - 1) - (10 ** (3 * k)) + 1) * k
                k += 1
        return count
