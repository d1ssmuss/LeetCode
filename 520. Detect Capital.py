class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper() or word.istitle() or word.islower():
            return True
        else:
            return False
        
