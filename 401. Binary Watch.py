class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        clock = []
        for h in range(0, 12):
            for m in range(0, 60):
                hh = bin(h)[2:]
                mm = bin(m)[2:]
                watch = str(h) + ":" + str(m).zfill(2)
                if (hh + mm).count('1') == turnedOn:
                    clock.append(watch)
        return clock
