import string
class Solution:
    def greatestLetter(self, s: str) -> str:
        mx = ""
        letters = set(s)
        for letter in letters:
            if letter.isupper() and letter.lower() in s:
                mx = max(mx, letter.upper())
        return mx
