# import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n <= 0:
        #     return False
        # else:
        #     x = math.log2(n)
        #     if x - int(x) != 0:
        #         return False
        #     else:
        #         return True
        x = bin(n)[2:]
        if x[0] == '1' and x[1:] == '0' * (len(x) - 1):
            return True
        else:
            return False



# for i in range(0, 65):
#     print(i, Solution().isPowerOfTwo(i))
# print(Solution().isPowerOfTwo(1))
# print(Solution().isPowerOfTwo(3))
# print(Solution().isPowerOfTwo(13))
# print(Solution().isPowerOfTwo(16))