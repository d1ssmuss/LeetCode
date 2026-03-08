class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        nums = [str(i) for i in nums]
        arr = []
        for i in range(len(nums)):
            num = nums[:i + 1]
            # print(num)
            if int(''.join(num), 2) % 5 == 0:
                arr.append(True)
            else:
                arr.append(False)
        return arr


print(Solution().prefixesDivBy5([0,1,1]))
print(Solution().prefixesDivBy5([1,1,1]))
print(Solution().prefixesDivBy5([1,1,0,0,0,1,0,0,1]))