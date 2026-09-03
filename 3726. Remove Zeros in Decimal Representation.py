class Solution:
    def removeZeros(self, n: int) -> int:
        str_n = str(n)
        str_n = str_n.replace('0', '')
        return int(''.join(str_n))
