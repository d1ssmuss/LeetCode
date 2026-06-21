class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        # count = 0
        # d = {i:costs.count(i) for i in set(costs)}
        # for k, v in d.items():
        #     if k <= coins:
        #         if v <= coins:
        #             coins -= (k * v)
        #             count += k * v
        #         else:
        #             coins -= (coins % k)
        #             count += coins % k
        #         print(k, v, coins, count)
        #     else:
        #         break
        # return count


        count = 0
        costs.sort()
        for i in costs:
            if coins > 0 and i <= coins:
                count += 1
                coins -= i
            else:
                break
        return count


print(Solution().maxIceCream(costs = [1,3,2,4,1], coins = 7))
print(Solution().maxIceCream([10,6,8,7,7,8], coins = 5))
print(Solution().maxIceCream(costs = [1,6,3,1,2,5], coins = 20))