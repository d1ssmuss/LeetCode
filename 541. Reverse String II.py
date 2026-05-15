class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        answ = ''
        for i in range(0, len(s), k):
            if i % (2 * k) == 0:
                # print(i, s[i:i+k])
                answ += s[i:i+k][::-1]
            else:
                answ += s[i:i+k]
        return answ
        
