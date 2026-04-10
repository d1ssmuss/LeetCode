class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for index, value in enumerate(nums):
            if value not in d:
                d[value] = []
            d[value].append(index)
        print(d)
        mn = float('+inf')
        for spisok in d.values():
            if len(spisok) >= 3:
                for index in range(len(spisok) - 2):
                    troika = spisok[index:index + 3]
                    # print(troika)
                    i = troika[0]
                    j = troika[1]
                    k = troika[2]
                    rs = abs(i - j) + abs(j - k) + abs(k - i)
                    mn = min(mn, rs)
        return mn if mn != float('+inf') else -1


print(Solution().minimumDistance(nums = [1,2,1,1,3]))
print(Solution().minimumDistance(nums = [1,1,2,3,2,1,2]))
print(Solution().minimumDistance(nums = [1]))
print(Solution().minimumDistance(nums = [1,1,1,1]))
