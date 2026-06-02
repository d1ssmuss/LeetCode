class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        mn = float('+inf')
        land = []
        water = []
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                if landStartTime[i] + landDuration[i] >= waterStartTime[j]:
                    land.append(landStartTime[i] + landDuration[i] + waterDuration[j])
                else:
                    land.append(waterStartTime[j] + waterDuration[j])
        for i in range(len(waterStartTime)):
            for j in range(len(landStartTime)):
                if waterStartTime[i] + waterDuration[i] >= landStartTime[j]:
                    water.append(waterStartTime[i] + waterDuration[i] + landDuration[j])
                else:
                    water.append(landStartTime[j] + landDuration[j])
        return min(min(land), min(water))
