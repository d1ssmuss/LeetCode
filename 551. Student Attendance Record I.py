class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = s.count('A')
        s = s.replace('P', '*').replace("A", "*").split('*')
        # print(max(s, key=len))
        if count < 2 and len(max(s, key=len)) < 3:
            return True
        else:
            return False


print(Solution().checkRecord("PPALLP"))
print(Solution().checkRecord("PPALLL"))
print(Solution().checkRecord("PLLPALLLLPAAPPLLPPAA"))