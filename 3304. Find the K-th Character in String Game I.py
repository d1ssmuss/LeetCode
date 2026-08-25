class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) <= k:
            letters = []
            for letter in word:
                letters.append(chr(ord(letter) + 1))
            word += ''.join(letters)
            print(word, letters)
        return word[k - 1]
