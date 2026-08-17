# class Solution: # 7 ms
#     def getSneakyNumbers(self, nums: List[int]) -> List[int]:
#         stack = []
#         answ = []
#         for i in nums:
#             if i not in stack:
#                 stack.append(i)
#             else:
#                 answ.append(i)
#         return answ
from collections import Counter # 0 ms
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        return [k for k, v in d.items() if v == 2]
