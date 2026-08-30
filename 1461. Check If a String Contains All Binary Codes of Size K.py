class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        all_t = set()
        for i in range(len(s) - k + 1):
            t = s[i:i + k]
            all_t.add(t)
        return True if len(all_t) == 2 ** k else False
