class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = 0
        for i in satones:
            if i in set(jewels):
                s += 1
        return s
