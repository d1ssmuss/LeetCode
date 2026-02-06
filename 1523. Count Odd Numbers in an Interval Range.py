class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # return (sum(1 for i in range(low, high + 1) if i % 2 != 0)), list((i for i in range(low, high + 1) if i % 2 != 0))
        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        else:
            return ((high - low) // 2) + 1


print(Solution().countOdds(3, 7))
print(Solution().countOdds(8, 10))
print(Solution().countOdds(1, 99))
print(Solution().countOdds(4, 8))
print(Solution().countOdds(2, 16))