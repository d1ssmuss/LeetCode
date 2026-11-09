from itertools import *
class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Я должен взять по 3 элемента
        nums = []
        d = ''.join([str(i) for i in digits])
        for num in list(set(itertools.permutations(d, 3))):
            if num[0] != '0' and int(num[2]) % 2 == 0:
                nums.append(int(num[0] + num[1] + num[2]))
        nums.sort()
        return nums
