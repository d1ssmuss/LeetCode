class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        return min(abs(30 * hour - 5.5 * minutes), 360 - abs(30 * hour - 5.5 * minutes))
