class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # сумма = сколько раз встречается каждый элемент
        # т.е по факту нужен сет?
        total_frequencies = 0
        max = -1
        numbers = list(set(nums)) # Преобразованный список, в котором нет дубликатов
        for i in nums:
            if max < nums.count(i):
                max = nums.count(i)
        # print(f"nums = {nums}, max = {max}, numbers = {numbers}")
        for i in nums:
            if nums.count(i) == max:
                total_frequencies += numbers.count(i)
        # return total_frequencies, max
        return total_frequencies


# t = Solution().maxFrequencyElements(nums=[1,2,2,3,1,4]) # 4
# t1 = Solution().maxFrequencyElements(nums=[1,2,3,4,5]) # 5
# t2 = Solution().maxFrequencyElements(nums=[10,12,11,9,6,19,11]) # 2
# print(t, t1, t2)
