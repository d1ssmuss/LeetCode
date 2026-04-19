class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        answ = []
        for word in words:
            nums = []
            for letter in word:
                if letter.lower() in 'qwertyuiop':
                    nums.append(1)
                elif letter.lower() in 'asdfghjkl':
                    nums.append(2)
                else:
                    nums.append(3)
            if len(set(nums)) == 1:
                answ.append(word)
        return answ
