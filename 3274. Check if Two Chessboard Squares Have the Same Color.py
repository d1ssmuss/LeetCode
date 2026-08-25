class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        letters = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
        coord_1 = int(letters[coordinate1[0]] + int(coordinate1[1]))
        coord_2 = int(letters[coordinate2[0]] + int(coordinate2[1]))
        if (coord_1 + coord_2) % 2 == 0:
            return True
        else:
            return False
