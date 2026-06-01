class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort(reverse = True)
        s = 0
        for i in range(len(cost)):
            if i % 3 != 2:
                s += cost[i]
        return s


print(Solution().minimumCost([1,2,3]))
print(Solution().minimumCost([6,5,7,9,2,2]))
print(Solution().minimumCost([5,5]))
