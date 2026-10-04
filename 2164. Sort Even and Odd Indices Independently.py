class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        odd = []
        even = []
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        odd.sort(reverse = True)
        even.sort()
        answ = []
        for i in range(len(nums)):
            if i % 2 == 0:
                answ.append(even[i // 2])
            else:
                answ.append(odd[i // 2])
        return answ
