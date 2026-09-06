class Solution:
    def isPalindromic(self, s: str) -> bool:
        result = ''
        for letter in s:
            result += bin(ord(letter))[2:].zfill(8)
        return True if result == result[::-1] else False
