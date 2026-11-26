class Solution:
    def canAliceWin(self, n: int) -> bool:
        f = True
        k = 10
        for i in range(9):
            if n < 0:
                return f
            else:
                if i % 2 == 0: # Bob wins
                    f = False
                else:
                    f = True
            n -= k
            k -= 1
        return f
