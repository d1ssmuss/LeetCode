import itertools
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        k = 0
        for i in list(set(itertools.permutations(digits, 3))):
            a = i[0]
            b = i[1]
            c = i[2]
            if a != 0 and c % 2 == 0:
                k += 1
        return k
