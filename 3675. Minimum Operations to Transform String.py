class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        # b -> a (так нельзя)
        unique_letters = sorted(list(set(s)))
        if 'a' in unique_letters:
            unique_letters.remove('a')
        count = 0
        while s != 'a' * len(s):
            for i in range(len(unique_letters) - 1):
                count += (ord(unique_letters[i+1]) - ord(unique_letters[i]))
                s = s.replace(unique_letters[i], unique_letters[i+1])
            count += 26 - (ord(unique_letters[-1]) - ord('a'))
            break
        return count
