from collections import Counter


class Solution(object):
    def lastNonEmptyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = Counter(s)
        mx = max([i-1 for i in d.values()])
        answ = ""
        d_count = {i : 0 for i in set(s)}
        for i in s:
            if d_count[i] < mx:
                d_count[i] += 1
            else:
                answ += i
        return answ





print(Solution().lastNonEmptyString("aabcbbca"))
print(Solution().lastNonEmptyString("abcd"))
