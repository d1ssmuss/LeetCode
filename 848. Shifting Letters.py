class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        letters = list(s)
        total_shift = 0
        for i in range(len(shifts) - 1, -1, -1):
            # print(f"letter: {letters[i]} : {ord(letters[i])}")
            total_shift += shifts[i]
            delta = ord(letters[i]) + (total_shift % 26)
            delta %= 97
            # print(f"delta: {delta}, delta % 26: {delta % 26}")
            # print(f"delta: {delta}, delta % 97: {delta % 97}")
            letters[i] = chr(ord('a') + delta % 26)
            # print(f"letter: {ord(letters[i])} : {letters[i]}")
        return ''.join(letters)

# a = Solution().shiftingLetters("bad", [10, 20, 30])
# b = Solution().shiftingLetters("abc", [3, 5, 9])
c = Solution().shiftingLetters("asd", [999, 999, 999])
# d = Solution().shiftingLetters("z", [1])
# e = Solution().shiftingLetters("z", [52])
# f = Solution().shiftingLetters("aaa", [1, 2, 3])
# print(a)
# print(b) # rpl
print(c) # hoo
# print(d)
# print(e) # z
# print(f)