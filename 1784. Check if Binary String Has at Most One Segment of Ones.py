class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if s.count('0') == 0:
            return True
        else:
            zero_index = s.index('0')
            if s[zero_index:].count('1') >= 1:
                return False
            else:
                return True
