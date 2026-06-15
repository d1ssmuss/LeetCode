from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        c = Counter(s)
        vowel = max((c[i] for i in set(s) if i in 'aeiou'), default=0)
        consonant = max((c[i] for i in set(s) if i not in 'aeiou'), default=0)
        return vowel + consonant
