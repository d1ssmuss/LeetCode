from itertools import permutations


class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        times = []
        for i in permutations(arr, 4):
            times.append("".join(map(str, i)))

        times.sort()
        # print(times)

        max_time = ''
        for time in times:
            hours = time[:2]
            minutes = time[2:]
            if (0 <= int(hours) <= 23 and 0 <= int(minutes) <= 59):
                # max_time = '00:00'
                max_time = hours + ":" + minutes
        return max_time


print(Solution().largestTimeFromDigits([8,2,0,7]))
print(Solution().largestTimeFromDigits([0,0,0,0]))
print(Solution().largestTimeFromDigits([4,4,4,4]))
print(Solution().largestTimeFromDigits([1,1,0,1]))