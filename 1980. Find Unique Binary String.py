from itertools import product


class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        """
        Учитывая массив строк nums, содержащий n уникальных двоичных строк, каждая длиной n, 
        верните двоичную строку длиной n, которая не отображается в nums. 
        Если ответов несколько, вы можете вернуть любой из них.
        """
        # print(sorted(nums))
        for i in range(0, 2 ** len(nums)):
            num = bin(i)[2:]
            if len(num) == len(nums) and num not in nums:
                return num
        else:
            return '0' * len(nums)


print(Solution().findDifferentBinaryString(["01","10"]))
print(Solution().findDifferentBinaryString(["00","01"]))
print(Solution().findDifferentBinaryString(["111","011","001"]))