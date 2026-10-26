class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        k = 0
        for word in words:
            # if word[0:len(pref)] == pref: # 1 ms why ???
            if word.startswith(pref):
                k += 1
        return k
