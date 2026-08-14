from collections import Counter
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        mx = -1
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                d = Counter(s[i:j + 1])
                # print(d.values())
                if all([True if el <= 2 else False for el in d.values() ]):
                    mx = max(mx, len(s[i:j + 1]))
                    # print(s[i:j + 1])
                else:
                    break
        return mx
