class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = 1
        flag = True
        while True:
            s = mx
            for i in nums:
                s += i
                if s < 1:
                    flag = False
            if flag == False:
                mx += 1
                flag = True
            else:
                return mx
