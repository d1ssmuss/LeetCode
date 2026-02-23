class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = int(dividend / divisor)
        if a > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif a < -2 ** 31:
            return -2 ** 31
        else:
            return a 
