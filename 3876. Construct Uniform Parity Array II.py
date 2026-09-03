# class Solution:
#     def uniformArray(self, nums1: list[int]) -> bool:
#         n = len(nums1)
#         even, odd = [], []
#         min_even, min_odd = float('+inf'), float('+inf')
#
#         # Находим минимумы чисел
#         for x in nums1:
#             if x % 2 == 0:
#                 min_even = min(min_even, x)
#             else:
#                 min_odd = min(min_odd, x)
#
#
#         # print(min_even, min_odd)
#
#         for num in nums1:
#             if num % 2 == 0:
#                 even.append(num)
#                 if (num - min_odd) >= 1 and (num - min_odd) % 2 != 0:
#                     odd.append(num - min_odd)
#             else:
#                 odd.append(num)
#                 if (num - min_even) >= 1 and (num - min_even) % 2 == 0:
#                     even.append(num - min_even)
#
#         # print(even, odd)
#         return True if len(odd) == n or len(even) == n else False
#
#
#
#
# while (data := list(map(int, input().split(',')))):
#     print(Solution().uniformArray(data))


# Оптимизация
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        even, odd = True, True
        min_even, min_odd = float('+inf'), float('+inf')

        # Находим минимумы чисел
        for x in nums1:
            if x % 2 == 0:
                min_even = min(min_even, x)
            else:
                min_odd = min(min_odd, x)

        for i in range(n):
            if nums1[i] % 2 == 0 and min_odd != float('+inf'):
                if (nums1[i] - min_odd) < 1 or (nums1[i] - min_odd) % 2 == 0:
                    odd = False
                    break
        for i in range(n):
            if nums1[i] % 2 != 0 and min_even != float('+inf'):
                if (nums1[i] - min_even) < 1 or (nums1[i] - min_even) % 2 != 0:
                    even = False
                    break
        print(nums1, odd, even)
        return odd or even
        # return True if (odd or even) else False




print(Solution().uniformArray([1, 4, 7])) # True
print(Solution().uniformArray([2, 3])) # False
print(Solution().uniformArray([4, 6])) # True
print(Solution().uniformArray([1,3,5,7,9,2,4,6,8])) # True
