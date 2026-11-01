class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # if len(set(nums)) == 1:
        #     return 0
        # else:
        #     k = 0
        #     # Находим максимум
        #     # Увеличиваем все числа кроме единичного максимума
        #     # Смотрим пока все числа не будут равны, продолжаем операции
        #     while len(set(nums)) != 1:
        #         mx_index = nums.index(max(nums))
        #         nums = [nums[i] + 1 if i != mx_index else nums[i] for i in range(len(nums))]
        #         k += 1
        #     return k
        # return sum(nums) - len(nums)
        mn = min(nums)
        k = 0
        for i in nums:
            if i != mn:
                k += i - mn
        return k
