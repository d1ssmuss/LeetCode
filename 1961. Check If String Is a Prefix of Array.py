class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        answ = ''
        for word in words:
            answ += word
            if answ == s:
                return True
        else:
            return False
