class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        else:
            for i in s1:
                if i not in s2:
                    return False
            a = s1[2] + s1[1] + s1[0] + s1[3]
            b = s1[0] + s1[3] + s1[2] + s1[1]
            c = s1[2] + s1[3] + s1[0] + s1[1]
            if c == s2 or s2 == a or s2 == b:
                return True
            else:
                return False
