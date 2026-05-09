class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pr = 1 if '0' not in str(n) else 0
        s = sum([int(i) for i in (str(n))])
        while n % 10 != 0:
            pr *= n % 10
            n //= 10
        return pr - s
