class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = [nums[0]]
        # d = []
        # for i in nums[1:]:
        #     if i in n:
        #         d.append(i)
        #     n.append(i)
        # return sum([i for i in n if i not in d])
        n = []
        r = []
        for i in nums:
            if i in n:
                r.append(i)
            n.append(i)
        return sum([i for i in n if i not in r])
            
