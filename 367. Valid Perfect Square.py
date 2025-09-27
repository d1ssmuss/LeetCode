class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        i = 2
        while i * i <= num:
            if i * i == num:
                return True
                break
            else:
                i += 1
        else:
            return False
