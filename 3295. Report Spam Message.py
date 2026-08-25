from collections import Counter
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        d = Counter(message)
        c = 0
        for banword in set(bannedWords):
            if banword in d.keys():
                c += d[banword]
            if c >= 2:
                return True
        else:
            return False
