class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        s = [0]
        for i in gain:
            s.append(s[-1] + i)
        return max(s)
