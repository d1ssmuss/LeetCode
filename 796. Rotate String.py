class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # if len(s) != len(goal):
        #     return False
        # # общий корень
        # kor = goal
        # while kor not in s:
        #     kor = kor[0:len(kor)-1]
        # print('Kor: ', kor, 'goal[len(kor):]', goal[len(kor):], s[len(kor):], s.index(kor), 's[:s.index(kor)]', s[:s.index(kor)])
        # print('остаток', s[:s.index(kor)])
        # print(s[:s.index(kor)], goal[len(kor):])
        # return True if s[:s.index(kor)] == goal[len(kor):] else False

        if len(s) != len(goal):
            return False
        for i in range(len(s) + 1):
            if s == goal:
                return True
            else:
                s = s[1:] + s[0]
        return False


print(Solution().rotateString('abcde', "cdeab")) # true
print('-' * 50)
print(Solution().rotateString("abcde", "abced")) # false
print('-' * 50)
print(Solution().rotateString('defdefdefabcabc', 'defdefabcabcdef'))
print('-' * 50)
print(Solution().rotateString('abcde', 'debac'))
print('-' * 50)
print(Solution().rotateString('aaca', 'aaac')) # общее aac ?