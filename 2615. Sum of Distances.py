import itertools

class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == len(set(nums)):
            return [0] * len(nums)
        else:
            d = {}
            arr = []
            for i in range(len(nums)):
                d.setdefault(nums[i], []).append(i)
            print('nums', nums, 'd', d, '!')
            for i in range(len(nums)):
                v = d[nums[i]]
                print(nums[i], v, list(itertools.accumulate(v)), '!')
                if len(v) == 1:
                    arr.append(0)
                else:
                    k = 0
                    for j in range(len(v)):
                        if v[j] != i:
                            k += abs(v[j] - i)
                    arr.append(k)
            return arr


# print(Solution().distance([1,3,1,1,2]))
print(Solution().distance([2,0,2,2,6,5,2]))
# print(Solution().distance([2,0,2,2,6,5,2]) == [11,0,7,7,0,0,13])
# print(Solution().distance([0,5,3]))