class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = []
        right = []
        s_left = 0
        s_right = 0
        for i in range(len(nums)):
            # print(nums[:i])
            s_left = nums[:i]
            # print(s_left, 1)
            if s_left == []:
                left.append(0)
            else:
                left.append(sum(s_left))
        nums = nums[::-1]
        for i in range(len(nums)):
            # print(nums[:i])
            s_right = nums[:i]
            # print(s_right, 1)
            if s_right == []:
                right.append(0)
            else:
                right.append(sum(s_right))
        right = right[::-1]
        # print(left, right)
        return [abs(left[i] - right[i]) for i in range(len(nums))]

print(Solution().leftRightDifference([10,4,8,3]))
print(Solution().leftRightDifference([1]))
