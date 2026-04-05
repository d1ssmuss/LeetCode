class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        pos_x, pos_y = 0, 0
        for move in moves:
            if move == "U":
                pos_y += 1
            elif move == "D":
                pos_y -= 1
            elif move == 'L':
                pos_x -= 1
            else:
                pos_x += 1
        return True if pos_x == pos_y == 0 else False
