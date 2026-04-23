class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        unique = []
        for word in words:
            code = ''
            for letter in word:
                code += morse['abcdefghijklmnopqrstuvwxyz'.index(letter)]
            if code not in unique:
                unique.append(code)
        return len(unique)
