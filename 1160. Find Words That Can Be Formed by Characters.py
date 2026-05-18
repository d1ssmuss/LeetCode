class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        sum = 0
        for word in words:
            flag = True
            for letter in word:
                if word.count(letter) <= chars.count(letter):
                    continue
                else:
                    flag = False
                    break
            if flag:
                sum += len(word)
        return sum

print(Solution().countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))
print(Solution().countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))
print(Solution().countCharacters(words = ["cat","bt","hat","tree"], chars = "atachtre"))