class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        r_y = abs(z - y)
        r_x = abs(z - x)
        if r_y == r_x:
            return 0
        elif r_y < r_x:
            return 2
        else:
            return 1
