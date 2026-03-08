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
        if '0' * len(nums) not in nums:
            return '0' * len(nums)
        else:
            for i in product('01', repeat=len(nums)):
                n = ''.join(i)
                if n not in nums:
                    return n


print(Solution().findDifferentBinaryString(["01","10"]))
print(Solution().findDifferentBinaryString(["00","01"]))
print(Solution().findDifferentBinaryString(["111","011","001"]))

