class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitSum, squareSum = 0, 0
        while n != 0:
            digitSum += n % 10
            squareSum += (n % 10) ** 2
            n //= 10
        return True if squareSum - digitSum >= 50 else False
