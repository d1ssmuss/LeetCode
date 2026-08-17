class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        for index in range(len(sentence)):
            if searchWord == sentence[index][:len(searchWord)]:
                return index + 1
        else:
            return -1
