class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        count = 0
        for num in range(num1, num2 + 1):
            n = str(num)
            for i in range(1, len(n) - 1):
                if (int(n[i]) > int(n[i-1]) and int(n[i]) > int(n[i+1])) or (int(n[i]) < int(n[i-1]) and int(n[i]) < int(n[i+1])):
                    count += 1
        return count
