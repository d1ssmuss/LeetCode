class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n) + str(n * 2) + str(n * 3)
        digits = set(s)
        return True if '0' not in digits and len(digits) == len(s) else False
