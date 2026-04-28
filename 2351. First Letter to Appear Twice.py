class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {i:0 for i in set(s)}
        for letter in s:
            if 2 not in d.values():
                d[letter] += 1
                prev = letter
            else:
                return prev
        return s[-1] # конец цикла, последняя буква не попадает, так что выводим её
