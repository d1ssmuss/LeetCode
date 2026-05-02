class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 0
        for i in range(1, n + 1):
            reverse_i = ''
            summ = 0
            for j in str(i):
                if j == '2':
                    reverse_i += '5'
                    summ += 1
                elif j == '5':
                    reverse_i += '2'
                    summ += 1
                elif j == '6':
                    reverse_i += '9'
                    summ += 1
                elif j == '9':
                    reverse_i += '6'
                    summ += 1
                elif j == '0':
                    reverse_i += '0'
                    summ += 1
                elif j == '1':
                    reverse_i += '1'
                    summ += 1
                elif j == '8':
                    reverse_i += '8'
                    summ += 1
                else:
                    reverse_i += j
            if str(i) != reverse_i and summ == len(str(reverse_i)):
                k += 1
        return k



print(Solution().rotatedDigits(857)) # 247
print(Solution().rotatedDigits(10)) # 4
print(Solution().rotatedDigits(1)) # 0
print(Solution().rotatedDigits(2)) # 1