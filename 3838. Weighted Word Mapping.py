import string

class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        letters = string.ascii_lowercase
        reverse_letters = letters[::-1]
        answ = ''
        for el in words:
            s = 0
            for letter in el:
                s += weights[letters.index(letter)]
            answ += reverse_letters[s % 26]
        return answ




print(Solution().mapWordWeights(words = ["abcd","def","xyz"], weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]))
print(Solution().mapWordWeights(words = ["a","b","c"], weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
print(Solution().mapWordWeights(words = ["abcd"], weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]))