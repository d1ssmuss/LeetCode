class Solution:
    def countAsterisks(self, s: str) -> int:
        s = s.split('|')
        k = 0
        for i in range(len(s)):
            if i % 2 == 0:
                k += s[i].count('*')
        return k
