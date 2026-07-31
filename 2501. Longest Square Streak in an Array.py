class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        numbers = set(nums)
        d = {i:[] for i in numbers}
        for num in numbers: # цикл работает не так как надо
            while True:
                d[num].append(num)
                if num ** 2 in numbers:
                    num **= 2
                else:
                    break
        return len(max(d.values(), key=len)) if len(max(d.values(), key=len)) >= 2 else -1


print(Solution().longestSquareStreak([4,3,6,16,8,2])) # 3
print(Solution().longestSquareStreak([2,3,5,6,7])) # -1
print(Solution().longestSquareStreak([3,9,81,6561])) # 4
print(Solution().longestSquareStreak([5,12,3,10,4,11,4,16,11])) # 2
