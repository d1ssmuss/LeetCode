class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {i:0 for i in nums if i % 2 == 0}
        for i in nums:
            if i % 2 == 0:
                d[i] += 1
        nums_with_frequency_one = [k for k,v in d.items() if v == 1]
        return nums_with_frequency_one[0] if nums_with_frequency_one != [] else -1



print(Solution().firstUniqueEven([3,4,2,5,4,6]))
print(Solution().firstUniqueEven([4,4]))
print(Solution().firstUniqueEven([2]))
print(Solution().firstUniqueEven([6, 10]))