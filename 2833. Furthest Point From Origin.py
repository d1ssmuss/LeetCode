class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        l_count = moves.count('L')
        r_count = moves.count('R')
        _count = moves.count('_')
        delta = l_count - r_count
        if delta > 0:
            moves = moves.replace('_', 'L')
            return moves.count('L') - moves.count('R')
        elif delta < 0:
            moves = moves.replace('_', 'R')
            return moves.count('R') - moves.count('L')
        else:
            return _count